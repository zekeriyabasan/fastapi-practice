from fastapi import Request


def log(tag="", message="", request:Request=None):
    with open("log.txt", "a+", encoding="utf-8") as f:
        f.write(f"{tag} : {message}\n : request_url: {request.url}")