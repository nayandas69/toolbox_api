from fastapi import APIRouter
from app.utils.utility_utils import convert_currency, convert_units

router = APIRouter()

@router.get("/currency-converter")
def currency_converter(amount: float, from_currency: str, to_currency: str):
    return convert_currency(amount, from_currency, to_currency)

@router.get("/unit-converter")
def unit_converter(value: float, from_unit: str, to_unit: str):
    return convert_units(value, from_unit, to_unit)
