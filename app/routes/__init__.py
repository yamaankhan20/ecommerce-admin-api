import importlib
import inspect
import pkgutil
from fastapi import APIRouter
from fastapi.routing import APIRoute

router = APIRouter()

HTTP_METHODS = ["get", "post", "put", "delete", "patch"]

def include_all_controllers():
    controller_pkg = "app.controllers"
    for _, module_name, _ in pkgutil.iter_modules(["app/controllers"]):
        module = importlib.import_module(f"{controller_pkg}.{module_name}")
        for name, cls in inspect.getmembers(module, inspect.isclass):
            if cls.__module__.startswith(controller_pkg):
                tag_name = module_name.replace("Controller", "").capitalize()
                prefix = f"/{module_name.replace('Controller', '').lower()}"
                instance = cls()

                for method_name, method in inspect.getmembers(cls, inspect.isfunction):
                    for verb in HTTP_METHODS:
                        if method_name.startswith(f"{verb}_"):
                            path = method_name[len(verb):]
                            path = path.replace("_", "/") or "/"
                            full_path = f"{prefix}{path}"
                            router.add_api_route(
                                full_path,
                                getattr(instance, method_name),
                                methods=[verb.upper()],
                                name=method_name,
                                tags = [tag_name]
                            )
                            print(f"Registering route: {verb.upper()} {full_path} → {method_name}")


include_all_controllers()
