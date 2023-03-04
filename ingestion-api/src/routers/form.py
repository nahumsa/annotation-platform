from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", tags=["ingestion"], response_class=HTMLResponse)
async def show_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@router.post("/submit/", tags=["ingestion"])
async def submit_text_entry(text_entry: str = Form(...)):
    # TODO: add data to the argilla server.
    return RedirectResponse(url="/results", status_code=303)

@router.get("/results", tags=["ingestion"], response_class=HTMLResponse)
async def results(request: Request):
    return templates.TemplateResponse("result.html", {"request": request})