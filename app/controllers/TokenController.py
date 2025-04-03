from fastapi import HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends, Query, Path
from fastapi.responses import JSONResponse
from typing import Dict, Union

from app.models.Launchpad import Launchpad
from app.db.session import get_db
from app.utils.decoraters.expose_routes import expose_route

class TokenController:
    
    @expose_route
    def get_all_tokens(self, db: Session = Depends(get_db)):
        try:
            all_tokens = db.query(Launchpad).all()

            return JSONResponse(status_code=200, content=all_tokens)

        except HTTPException as e:
            return JSONResponse(status_code=e.status_code, content={"error": e.detail})

        except Exception as e:
            return JSONResponse(status_code=500, content={"error": str(e)})