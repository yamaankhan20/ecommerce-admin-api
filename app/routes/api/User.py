from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.db.session import get_db
from app.controllers.AuthController import create_user


class UserRoutes:
    def __init__(self):
        self.router = APIRouter(
            prefix="/users",
            tags=["Users"],
        )
        self._add_routes()

    def _add_routes(self):
        self.router.add_api_route('/fetch/{user_id}', self.get_user, methods=["GET"])
        self.router.add_api_route('/insert/', self.insert_user, methods=["POST"])

    async def get_user(self, user_id: int):
        return {"user_id": user_id}

    async def insert_user(self):
        return "done"


user_routes = UserRoutes()
router = user_routes.router
