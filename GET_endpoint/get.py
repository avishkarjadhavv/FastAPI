from fastapi import FastAPI

aj = FastAPI()

@aj.get("/")
def home():
    return {"message" : "hello"}

@aj.get("/contact")
def contact():
    return "You can contact us anytime"