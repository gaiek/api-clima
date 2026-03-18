from fastapi import FastAPI
from app.routes.clima import router as clima_router

app = FastAPI()
app.include_router(clima_router)