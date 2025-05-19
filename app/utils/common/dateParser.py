from datetime import datetime
from fastapi import HTTPException

def parse_date_safe(date_str: str) -> datetime:
    try:
        return datetime.fromisoformat(date_str)
    except ValueError:
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")  # fallback
        except ValueError:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid date format or out-of-range values: {date_str}. Use YYYY-MM-DD."
            )
