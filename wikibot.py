import wikipedia
import fastapi
import uvicorn
from pydantic import BaseModel

app = fastapi.FastAPI()


class ScrapeRequest(BaseModel):
    name: str
    length: int


@app.post("/scrape")
async def ScrapeWikipedia(request: ScrapeRequest):
    try:
        summary = wikipedia.summary(request.name, sentences=request.length)
        return {"summary": summary}
    except Exception as e:
        return {"error": str(e)}


@app.get("/")
async def root():
    return {"message": "Welcome to the Wikibot Microservice!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
