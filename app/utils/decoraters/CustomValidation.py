from fastapi.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

async def validation_exception_handler(request, exc):
    # Custom error message for missing path/query/body params
    errors = exc.errors()
    details = []

    for err in errors:
        loc = err.get("loc", [])
        msg = err.get("msg", "")
        if "path" in loc:
            param = loc[-1]
            details.append(f"Missing path parameter: `{param}`")
        else:
            details.append(msg)

    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content={"error": details or "Invalid request data"},
    )
