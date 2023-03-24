from fastapi import FastAPI

from src.routers import data

app = FastAPI()
app.include_router(data.router)
