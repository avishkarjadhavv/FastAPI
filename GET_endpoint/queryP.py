from fastapi import FastAPI , Request

app = FastAPI()

# @app.get("/greet")
# def greet(name:str , age:int):
#     return {"greet" : f"Hello {name}, your age is {age} "}

@app.get("/greet1")
def greet(request:Request):
    query_params = dict(request.query_params)
    return {"greet" : f"Hello {query_params.get("name")}, your age is {query_params.get("age")} "}