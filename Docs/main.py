from fastapi import FastAPI 
from router import router

app = FastAPI()

@app.get('/')
async def root():
    return "Hello World"
    
app.include_router(router)
