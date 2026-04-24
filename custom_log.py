def log(tag="", message=""):
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"{tag} : {message}\n")