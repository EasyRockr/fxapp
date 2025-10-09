from pydantic import BaseModel

class Rates(BaseModel):
    source:str
    target:str
    rates:float
