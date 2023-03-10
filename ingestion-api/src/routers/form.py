from fastapi import APIRouter, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="src/templates")


@router.get("/", tags=["ingestion"], response_class=HTMLResponse)
async def show_form(request: Request) -> HTMLResponse:
    """Shows a form that could be filled to be added to the annotation service.

    Args:
        request (Request): request received.

    Returns:
        HTMLResponse: webpage.
    """
    return templates.TemplateResponse("form.html", {"request": request})


@router.post("/submit/", tags=["ingestion"])
async def submit_text_entry(text_entry: str = Form(...)) -> RedirectResponse:
    """Submitts the text entry to the annotation service.

    Args:
        text_entry (str, optional): text entry from the form that is in "/". Defaults to Form(...).

    Returns:
        RedirectResponse: Redirects to /results.
    """
    # TODO: add data to the argilla server.
    return RedirectResponse(url="/results", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/results", tags=["ingestion"], response_class=HTMLResponse)
async def results(request: Request) -> HTMLResponse:
    """Shows a results page.

    Args:
        request (Request): request received.

    Returns:
        HTMLResponse: results webpage.
    """
    return templates.TemplateResponse("result.html", {"request": request})
