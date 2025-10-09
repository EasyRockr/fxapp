from fastapi import APIRouter, Response
from bll.rates_bll import RatesBll
from domain.service_response import ServiceResponse
from util.logger import enable_logging

router = APIRouter(tags=["Convert API"])
rates_bll = RatesBll("json")

@router.get("/convert/{source}/{target}/{amount}")
@enable_logging
def convert_currency(source: str, target: str, amount: float, response: Response) -> ServiceResponse[float]:
    res = ServiceResponse()
    try:
        converted = rates_bll.convert_amount(source, target, amount)
        res.data = converted
        res.status_message = f"Converted {amount} {source.upper()} to {converted} {target.upper()}"
        response.status_code = 200
    except ValueError as ex:
        res.status_code = 400
        res.status_message = str(ex)
        response.status_code = 200             
    except Exception as ex:
        res.status_code = 500
        res.status_message = str(ex)
        response.status_code = 500           
    return res
