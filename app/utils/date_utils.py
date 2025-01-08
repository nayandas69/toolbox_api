from datetime import datetime

def date_difference(date1: str, date2: str) -> int:
    date_format = "%Y-%m-%d"
    d1 = datetime.strptime(date1, date_format)
    d2 = datetime.strptime(date2, date_format)
    return abs((d2 - d1).days)

def current_day_info() -> dict:
    now = datetime.now()
    return {
        "day": now.strftime("%A"),
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S")
    }
