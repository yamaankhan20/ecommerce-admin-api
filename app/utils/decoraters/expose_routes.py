def expose_route(response_model=None):
    def decorator(func):
        setattr(func, "_exposed_route", True)
        setattr(func, "_response_model", response_model)  # 🔥 attach response model for Swagger
        return func
    return decorator