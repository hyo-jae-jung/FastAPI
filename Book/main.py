from fastapi import FastAPI
import uvicorn
from todo import todo_router

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {
        "message": "Hello World"
    }


app.include_router(todo_router)

if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.1", port=8002, reload=True)
