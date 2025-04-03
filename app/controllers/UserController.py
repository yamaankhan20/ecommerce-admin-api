from fastapi import HTTPException
from app.models.User import User
from typing import Dict, Union
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

            all_user_data: Dict[str, Union[str, int, None]] = {
                "name":user.name,
                "address":user.address,
                "profile_pic":user.profile_photo_path,
                "short_description": (user.description[:150] + "...") if user.description and len(
                    user.description) > 250 else user.description,
                "description": user.description,
                "website": user.website,
                "twitter": user.twitter,
                
            }

            return JSONResponse(status_code=200, content=all_user_data)

        except HTTPException as e:
            return JSONResponse(status_code=e.status_code, content={"error": e.detail})

        except Exception as e:
            return JSONResponse(status_code=500, content={"error": str(e)})


