import random
import string
import uuid

def generate_random_number(start: int, end: int) -> int:
    return random.randint(start, end)

def generate_random_string(length: int) -> str:
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_password(length: int) -> str:
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))

def generate_uuid() -> str:
    return str(uuid.uuid4())

def generate_hex_color() -> str:
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))
