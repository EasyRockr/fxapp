from fastapi import FastAPI
from controller.convert_api import router as convert_router
from controller.rates_api import router as rates_router

app = FastAPI()
api_app = FastAPI()

api_app.include_router(convert_router)
api_app.include_router(rates_router)
app.mount("/api/v1", api_app)
