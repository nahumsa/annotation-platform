import argilla as rg
from fastapi import APIRouter, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from src.configs import read_config_file

router = APIRouter()
templates = Jinja2Templates(directory="src/templates")
configs = read_config_file("src/configs.toml")


@router.get("/", tags=["ingestion"], response_class=HTMLResponse)
async def show_form(request: Request) -> HTMLResponse:
    """Shows a form that could be filled to be added to the annotation service.

    Args:
        request (Request): request received.

    Returns:
        HTMLResponse: webpage.
    """
    return templates.TemplateResponse("form.html", {"request": request})  # type: ignore


@router.post("/submit/", tags=["ingestion"])
async def submit_text_entry(text_entry: str = Form(...)) -> RedirectResponse:
    """Submitts the text entry to the annotation service.

    Args:
        text_entry (str, optional): text entry from the form that is in "/". Defaults to Form(...).

    Returns:
        RedirectResponse: Redirects to /results.
    """

    rg.init(**configs.argilla.dict())

    record = rg.TextClassificationRecord(
        text=text_entry,
        multi_label=False,
    )

    rg.log(
        records=record,
        name=configs.dataset.name,
        tags=configs.dataset.tags,
        background=configs.dataset.background,
        verbose=False,
    )

    return RedirectResponse(url="/results", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/results", tags=["ingestion"], response_class=HTMLResponse)
async def results(request: Request) -> HTMLResponse:
    """Shows a results page.

    Args:
        request (Request): request received.

    Returns:
        HTMLResponse: results webpage.
    """
    return templates.TemplateResponse("result.html", {"request": request})  # type: ignore
