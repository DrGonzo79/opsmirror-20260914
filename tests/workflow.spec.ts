import { test, expect } from "@playwright/test";
test("runs the primary audit and verifies a finding", async ({page})=>{
 await page.goto("/");
 await page.getByRole("button",{name:/run refund audit/i}).click();
 await expect(page.getByRole("status")).toContainText("6 decisions checked");
 await page.getByRole("button",{name:/SUP-1842/}).click();
 await expect(page.locator(".signals").getByText("Manager approval missing",{exact:true})).toBeVisible();
 await page.getByRole("button",{name:"Mark human-verified"}).click();
 await expect(page.getByRole("button",{name:"Undo verification"})).toBeVisible();
});
test("validates and adds a new demo decision",async({page})=>{
 await page.goto("/");
 await page.getByRole("button",{name:/add demo decision/i}).click();
 await expect(page.locator(".error")).toContainText("greater than $0");
 await page.getByLabel("Refund amount").fill("225");
 await page.getByRole("button",{name:/add demo decision/i}).click();
 await expect(page.getByRole("button",{name:/DEMO-7/})).toBeVisible();
 await expect(page.locator(".signals").getByText("Manager approval missing",{exact:true})).toBeVisible();
});
test("mobile layout has no horizontal overflow",async({page})=>{
 await page.setViewportSize({width:375,height:812}); await page.goto("/");
 const widths=await page.evaluate(()=>({scroll:document.documentElement.scrollWidth,client:document.documentElement.clientWidth}));
 expect(widths.scroll).toBeLessThanOrEqual(widths.client);
 await page.getByRole("button",{name:/run refund audit/i}).click();
 await expect(page.getByRole("status")).toBeVisible();
});
