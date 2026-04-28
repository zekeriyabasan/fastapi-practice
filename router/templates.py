from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix='/templates',
    tags=['templates']
)



templates = Jinja2Templates(directory="templates")

@router.get('/{id}', response_class = HTMLResponse)
def get_oopsie_info(id:str, request: Request):
    print(type(templates))
    return templates.TemplateResponse(
       name="oopsie.html",
       request=request,
       context={
           "id":id
       }
    )