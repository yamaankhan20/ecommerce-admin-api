class UserController:
    def get_info(self):
        return {"msg": "get user info"}

    def post_create(self):
        return {"msg": "user created"}

    def put_update(self):
        return {"msg": "user updated"}

    def delete_remove(self):
        return {"msg": "user removed"}