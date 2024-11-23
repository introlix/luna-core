from fastapi import FastAPI, Query, HTTPException
from src.luna.app.routes import luna

app = FastAPI()

app.include_router(luna.router)