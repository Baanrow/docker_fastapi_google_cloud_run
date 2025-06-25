from playwright.async_api import async_playwright
from pathlib import Path
from datetime import datetime, time
import time
from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/api")
async def process_browser_call(payload: Request):
    payload_content = await payload.json()
    if "XXXXX" in payload_content.values():
        await run_browser()
        return {"status": "Call success!"}
    return {"status": "Not allowed!!"}


async def run_browser():
    url = Path(f"screenshots/{datetime.now().strftime('%Y%m%d%H%M%S')}.jpg")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://www.yoururl.com/")
        locator = page.locator("text=CONTACT").first
        await locator.click()
        await page.screenshot(path=url)
        await browser.close()
