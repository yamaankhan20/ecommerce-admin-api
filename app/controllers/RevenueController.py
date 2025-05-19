from fastapi import Depends, HTTPException, Query
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from datetime import datetime, timedelta
from fastapi.encoders import jsonable_encoder

from app.db.session import get_db
from app.models.Sales import Sales
from app.models.Product import Products
from app.utils.decoraters.expose_routes import expose_route

class RevenueController:

    @expose_route()
    def get_revenue_summary(self, period: str = Query(...), db: Session = Depends(get_db)):
        try:
            now = datetime.now()
            if period == "daily":
                start = now.replace(hour=0, minute=0, second=0, microsecond=0)
            elif period == "weekly":
                start = now - timedelta(days=now.weekday())
            elif period == "monthly":
                start = now.replace(day=1)
            elif period == "annual":
                start = now.replace(month=1, day=1)
            else:
                raise HTTPException(status_code=400, detail="Invalid period format. Use: daily, weekly, monthly, annual")

            revenue = db.query(func.sum(Sales.price * Sales.quantity)).filter(Sales.sale_date >= start).scalar() or 0

            return JSONResponse(
                status_code=200,
                content={
                    "message": f"{period.capitalize()} revenue calculated successfully",
                    "data": {"revenue": float(revenue)}
                }
            )


        except HTTPException as e:
            return JSONResponse(status_code=e.status_code, content={"error": e.detail})

        except Exception as e:
            return JSONResponse(status_code=500, content={"error": str(e)})


    @expose_route()
    def get_revenue_compare(
        self,
        period1: str = Query(...),
        period2: str = Query(...),
        category_id: int = Query(None),
        db: Session = Depends(get_db)
    ):
        try:
            def get_start_date(period: str):
                now = datetime.now()
                if period == "daily":
                    return now.replace(hour=0, minute=0, second=0, microsecond=0)
                elif period == "weekly":
                    return now - timedelta(days=now.weekday())
                elif period == "monthly":
                    return now.replace(day=1)
                elif period == "annual":
                    return now.replace(month=1, day=1)
                else:
                    raise HTTPException(status_code=400, detail=f"Invalid period: {period}")

            result = {}
            for period in [period1, period2]:
                start = get_start_date(period)
                query = db.query(func.sum(Sales.price * Sales.quantity))

                if category_id:
                    query = query.join(Products).filter(Products.category_id == category_id)

                total = query.filter(Sales.sale_date >= start).scalar() or 0
                result[period] = float(total)

            return JSONResponse(
                status_code=200,
                content={
                    "message": "Revenue comparison successful",
                    "data": result
                }
            )


        except HTTPException as e:
            return JSONResponse(status_code=e.status_code, content={"error": e.detail})

        except Exception as e:
            return JSONResponse(status_code=500, content={"error": str(e)})
