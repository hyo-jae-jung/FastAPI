from fastapi import FastAPI
from crud_test_router import crud_test_router

app = FastAPI()

@app.get('/')
async def root():
    return "Hello World!!"

app.include_router(crud_test_router)
