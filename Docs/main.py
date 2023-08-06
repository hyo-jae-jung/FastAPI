from fastapi import FastAPI, Request
from router import router
from fastapi.templating import Jinja2Templates
app = FastAPI()
templates = Jinja2Templates(directory="templates/")

val = 'Hello World!!'

@app.get('/')
async def root(request: Request):
    return templates.TemplateResponse("home.html",{
        "request":request,
        "val": val
        })
    
app.include_router(router)
