import shutil

from fastapi import APIRouter, File, UploadFile

router = APIRouter(
    tags = ['file'],
    prefix = '/file'

)

@router.post('/view-file-content')
def get_file_content(file:bytes = File(...)):
    content = file.decode('utf-8')
    lines = content.split('\n')
    return {
        "lines":lines
    }

@router.post('/upload')
def get_uploadfile(upload_file:UploadFile = File(...)):
    path = f"files/{upload_file.filename}"

    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(upload_file.file, buffer) # copy the file into the path

    return {
        'file_path':path,
        'type':upload_file.content_type
    }