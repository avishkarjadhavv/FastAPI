from fastapi import FastAPI

aj = FastAPI(title="This is my Task Management Application")

@aj.get("/")
def greet():
    return "Hello , you're welcome to Task Management Application"