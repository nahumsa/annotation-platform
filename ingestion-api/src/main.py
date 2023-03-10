from fastapi import FastAPI

from src.routers import form

app = FastAPI()
app.include_router(form.router)
