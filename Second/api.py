from fastapi import FastAPI, Request
import uvicorn
from fastapi.templating import Jinja2Templates
from todo import todo_router

app = FastAPI()

templates = Jinja2Templates(directory="templates/")

@app.get("/")
async def welcome(request: Request) -> dict:
    return templates.TemplateResponse("home.html",
    {
        "request":request,
    })

app.include_router(todo_router)

if __name__ == "__main__":
    uvicorn.run("api:app",host="127.0.0.1", port=8001, reload=True)
