from fastapi import FastAPI
from routers import helloworld

app = FastAPI()

app.include_router(helloworld.router)

@app.get('/')
async def root():
    return "Hello world"