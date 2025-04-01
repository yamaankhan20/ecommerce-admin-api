from fastapi import HTTPException
from app.models.User import User
from app.schemas.user_schema import UserResponse  # if needed
from sqlalchemy.orm import Session
from fastapi import Depends, Query, Path
from app.db.session import get_db
from app.utils.decoraters.expose_routes import expose_route
from fastapi.responses import JSONResponse

class UserController:

    @expose_route()
    def get_user_info_single(self, db: Session = Depends(get_db), user_id: int = Path(...) ):
        try:
            user = db.query(User).filter_by(id=user_id).first()

            if not user:
                raise HTTPException(status_code=404, detail="User not found")

            all_user_data: dict[str, str | int] = {
                "name":user.name,
                "address":user.address,
                "profile_pic":user.profile_pic,
            }

            return all_user_data
        except Exception as e:
            return JSONResponse(status_code=500, content={"error": f"{str(e.detail)}"})


