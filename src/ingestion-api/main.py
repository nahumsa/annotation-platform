from fastapi import FastAPI
from routers import form

app = FastAPI()
app.include_router(form.router)