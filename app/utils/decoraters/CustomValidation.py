from fastapi.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

async def validation_exception_handler(request, exc):
    errors = exc.errors()
    details = {}

    for err in errors:
        loc = err.get("loc", [])
        msg = err.get("msg", "")
        field = loc[-1] if loc else "unknown"

        if loc[0] in {"body", "query", "path"}:
            details[field] = f"{field} {msg}"
        else:
            details[field] = msg

    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content={"error": details or "Invalid request data"},
    )
