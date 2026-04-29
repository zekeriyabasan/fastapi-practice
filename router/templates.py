from fastapi import APIRouter, BackgroundTasks, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import custom_log
from db.schemas import OopsieBase

router = APIRouter(
    prefix='/templates',
    tags=['templates']
)



templates = Jinja2Templates(directory="templates")

@router.get('/{id}', response_class = HTMLResponse )
def get_oopsie_info(id:str, request: Request,  bt: BackgroundTasks):
    bt.add_task(log_template_call, f"Template read for oopsie with id {id}")
    return templates.TemplateResponse(
       name="oopsie.html",
       request=request,
       context={
           "id":id
       }
    )

@router.post('/', response_class = HTMLResponse)
def get_oopsie_info(oopsie:OopsieBase , request: Request):
    print(type(templates))
    return templates.TemplateResponse(
       name="oopsie.html",
       request=request,
       context={
           "title":oopsie.title,
           "description":oopsie.description,
           "assigned_user":oopsie.assigned_user
       }
    )

def log_template_call(message: str):
    custom_log.log("MyAPI", message)