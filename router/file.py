from fastapi import APIRouter, File

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