from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
def test_health(): assert client.get("/health").json() == {"status":"ok"}
def test_demo_fixture_contract():
    result = client.get("/demo")
    assert result.status_code == 200
    assert result.json()["checked"] == 6
    assert result.json()["driftCount"] == 5
    assert result.json()["gapCount"] == 6
def test_real_audit_operation():
    payload={"policy":{"managerThreshold":100,"evidenceThreshold":50,"responseSlaHours":24,"requiredReason":True},"tickets":[{"id":"T-1","customer":"Demo","amount":200,"reason":"","managerApproved":False,"evidenceAttached":False,"responseHours":30,"agent":"A"}]}
    body=client.post("/audit",json=payload).json()
    assert body["gapCount"] == 4
    assert body["findings"][0]["status"] == "drift"
def test_invalid_and_empty_inputs():
    base={"policy":{"managerThreshold":100,"evidenceThreshold":50,"responseSlaHours":24,"requiredReason":True},"tickets":[]}
    assert client.post("/audit",json=base).status_code == 422
    base["tickets"]=[{"id":"T","customer":"Demo","amount":-1,"reason":"x","managerApproved":True,"evidenceAttached":True,"responseHours":1,"agent":"A"}]
    assert client.post("/audit",json=base).status_code == 422
