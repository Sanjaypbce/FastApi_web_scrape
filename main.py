from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl

from scraper import scrape

app = FastAPI()

class ScrapeRequest(BaseModel):
    url: HttpUrl

@app.post("/scrape")
def scrape_website(scrape_request: ScrapeRequest):
    result = scrape(scrape_request.url)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result
