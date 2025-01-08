from fastapi import APIRouter
from app.utils.date_utils import date_difference, current_day_info

router = APIRouter()

@router.get("/date-difference")
def calculate_date_difference(date1: str, date2: str):
    return {"days_difference": date_difference(date1, date2)}

@router.get("/current-day-info")
def get_current_day_info():
    return current_day_info()
