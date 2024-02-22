"""Api entrypoint file"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def hello_world():
    """Project initializing endpoint"""
    return "hello world"
