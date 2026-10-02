from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()

from app.database import init_db
from app.routes import router

app = FastAPI(title="FitBuddy - AI Fitness Generator")

init_db()

app.include_router(router)