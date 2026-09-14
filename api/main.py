from enum import Enum
from pathlib import Path
import json
from fastapi import FastAPI
from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parents[1]
app = FastAPI(title="OpsMirror API", version="0.1.0")

class GapCode(str, Enum):
    APPROVAL_MISSING = "APPROVAL_MISSING"
    EVIDENCE_MISSING = "EVIDENCE_MISSING"
    REASON_MISSING = "REASON_MISSING"
    SLA_BREACH = "SLA_BREACH"

class Policy(BaseModel):
    managerThreshold: float = Field(gt=0, le=10000)
    evidenceThreshold: float = Field(ge=0, le=10000)
    responseSlaHours: int = Field(gt=0, le=720)
    requiredReason: bool = True

class Ticket(BaseModel):
    id: str = Field(min_length=1, max_length=50)
    customer: str = Field(min_length=1, max_length=120)
    amount: float = Field(gt=0, le=10000)
    reason: str = Field(max_length=500)
    managerApproved: bool
    evidenceAttached: bool
    responseHours: int = Field(ge=0, le=10000)
    agent: str = Field(min_length=1, max_length=80)

class AuditRequest(BaseModel):
    policy: Policy
    tickets: list[Ticket] = Field(min_length=1, max_length=500)

def inspect(ticket: Ticket, policy: Policy) -> list[GapCode]:
    gaps: list[GapCode] = []
    if ticket.amount > policy.managerThreshold and not ticket.managerApproved:
        gaps.append(GapCode.APPROVAL_MISSING)
    if ticket.amount > policy.evidenceThreshold and not ticket.evidenceAttached:
        gaps.append(GapCode.EVIDENCE_MISSING)
    if policy.requiredReason and not ticket.reason.strip():
        gaps.append(GapCode.REASON_MISSING)
    if ticket.responseHours > policy.responseSlaHours:
        gaps.append(GapCode.SLA_BREACH)
    return gaps

@app.get("/health")
def health() -> dict[str, str]: return {"status": "ok"}

@app.post("/audit")
def audit(request: AuditRequest) -> dict:
    findings = [{"ticketId": t.id, "status": "drift" if (gaps := inspect(t, request.policy)) else "aligned", "gaps": gaps} for t in request.tickets]
    return {"checked": len(findings), "driftCount": sum(f["status"] == "drift" for f in findings), "gapCount": sum(len(f["gaps"]) for f in findings), "findings": findings}

@app.get("/demo")
def demo() -> dict:
    policy_raw = json.loads((ROOT / "data/policy.json").read_text())
    policy_raw.pop("name", None)
    tickets = json.loads((ROOT / "data/tickets.json").read_text())
    return audit(AuditRequest(policy=Policy(**policy_raw), tickets=[Ticket(**t) for t in tickets]))
