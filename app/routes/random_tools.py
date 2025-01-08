from fastapi import APIRouter
from app.utils.random_utils import generate_random_number, generate_random_string, generate_password, generate_uuid, generate_hex_color

router = APIRouter()

@router.get("/random-number")
def random_number(start: int, end: int):
    return {"random_number": generate_random_number(start, end)}

@router.get("/random-string")
def random_string(length: int):
    return {"random_string": generate_random_string(length)}

@router.get("/random-password")
def random_password(length: int = 12):
    return {"random_password": generate_password(length)}

@router.get("/uuid")
def random_uuid():
    return {"uuid": generate_uuid()}

@router.get("/hex-color")
def random_hex_color():
    return {"hex_color": generate_hex_color()}
