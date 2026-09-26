from fastapi import FastAPI
from src.utils.db import Base , engine

Base.metadata.create_all(engine)


aj = FastAPI(title="This is my Task Management Application")


