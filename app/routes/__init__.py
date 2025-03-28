import importlib
import inspect
import pkgutil
from fastapi import APIRouter
from fastapi.params import Path
from app.utils.decoraters.expose_routes import expose_route

router = APIRouter()
HTTP_METHODS = ["get", "post", "put", "delete", "patch"]

def include_all_controllers():
    controller_pkg = "app.controllers"

    for _, module_name, _ in pkgutil.iter_modules(["app/controllers"]):
        module = importlib.import_module(f"{controller_pkg}.{module_name}")

        for name, cls in inspect.getmembers(module, inspect.isclass):
            if cls.__module__.startswith(controller_pkg):
                instance = cls()
                methods_to_register = [
                    (method_name, method)
                    for method_name, method in inspect.getmembers(cls, inspect.isfunction)
                    if getattr(method, "_exposed_route", False)
                ]

                if not methods_to_register:
                    continue

                tag_name = module_name.replace("Controller", "").capitalize()
                prefix = f"/{module_name.replace('Controller', '').lower()}"

                for method_name, method in methods_to_register:
                    for verb in HTTP_METHODS:
                        if method_name.startswith(f"{verb}_"):
                            path = method_name[len(verb):].lstrip("_")
                            path = path.replace("_", "-") or "/"

                            sig = inspect.signature(method)
                            path_params = [
                                f"{{{name}}}" for name, param in sig.parameters.items()
                                if isinstance(param.default, Path)
                            ]

                            full_path = f"{prefix}/{path}".rstrip("/")
                            if path_params:
                                full_path += "/" + "/".join(path_params)

                            response_model = getattr(method, "_response_model", None)

                            router.add_api_route(
                                full_path,
                                getattr(instance, method_name),
                                methods=[verb.upper()],
                                name=method_name,
                                tags=[tag_name],
                                response_model=response_model  # ✅ important!
                            )

                            print(f"✅ Registered: {verb.upper()} {full_path} → {method_name}")


include_all_controllers()
