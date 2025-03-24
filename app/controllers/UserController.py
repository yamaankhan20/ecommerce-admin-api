from app.utils.decoraters.expose_routes import expose_route

class UserController:

    @expose_route()
    def get_info(self):
        return {"msg": "get user info"}

    @expose_route()
    def post_create(self):
        return {"msg": "user created"}

    @expose_route()
    def put_update(self):
        return {"msg": "user updated"}

    @expose_route()
    def delete_remove(self):
        return {"msg": "user removed"}