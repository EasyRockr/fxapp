from fastapi import APIRouter
from bll.rates_bll import RatesBll
from domain.service_response import ServiceResponse
from util.logger import enable_logging


router = APIRouter(tags=["Rates API"])
rates_bll = RatesBll("json")

@router.get("/view-rates", response_model=ServiceResponse[dict])
@enable_logging
def retrieve_rates():
    response = ServiceResponse()
    try:
        response.data = rates_bll.get_rates_data()
    except Exception as ex:
        response.status_code = 500
        response.status_message = str(ex)
        response.data = None
    return response
