from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import helloworld, authentication
from fastapi.responses import JSONResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app.include_router(helloworld.router)
app.include_router(authentication.router)

@app.get('/')
async def root():
    return "Hello world2"