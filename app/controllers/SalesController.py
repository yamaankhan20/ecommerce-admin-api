import re
from fastapi import Depends, HTTPException, Query, Body
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional
from sqlalchemy.exc import IntegrityError

from app.db.session import get_db
from app.models.Sales import Sales
from app.models.Product import Products
from app.schemas.sale import SaleResponse, SaleCreate
from app.utils.decoraters.expose_routes import expose_route
from app.utils.common.dateParser import parse_date_safe

class SaleController:

    @expose_route()
    def get_sales(self, db: Session = Depends(get_db)):
        try:
            sales = db.query(Sales).all()

            if not sales:
                raise HTTPException(status_code=404, detail="No sales found")

            response_data = jsonable_encoder([
                SaleResponse.model_validate(s) for s in sales
            ])

            return JSONResponse(
                status_code=200,
                content={
                    "message": "Sales retrieved successfully",
                    "data": response_data
                }
            )

        except HTTPException as e:
            return JSONResponse(status_code=e.status_code, content={"error": e.detail})

        except Exception as e:
            return JSONResponse(status_code=500, content={"error": str(e)})

    @expose_route()
    def get_sales_filter(self, db: Session = Depends(get_db), start_date: Optional[str] = Query(None), end_date: Optional[str] = Query(None), product_id: Optional[int] = Query(None), category_id: Optional[int] = Query(None)
    ):
        try:
            query = db.query(Sales)

            if start_date:
                query = query.filter(Sales.sale_date >= parse_date_safe(start_date))
            if end_date:
                query = query.filter(Sales.sale_date <= parse_date_safe(end_date))
            if product_id:
                query = query.filter(Sales.product_id == product_id)
            if category_id:
                query = query.join(Products).filter(Products.category_id == category_id)

            results = query.all()
            if not results:
                raise HTTPException(status_code=404, detail="No matching sales found")

            response_data = jsonable_encoder([
                SaleResponse.model_validate(r) for r in results
            ])

            return JSONResponse(
                status_code=200,
                content={
                    "message": "Filtered sales retrieved successfully",
                    "data": response_data
                }
            )

        except HTTPException as e:
            return JSONResponse(status_code=e.status_code, content={"error": e.detail})
        except Exception as e:
            return JSONResponse(status_code=500, content={"error": str(e)})

    @expose_route()
    def post_create_sale(self, db: Session = Depends(get_db), sale: SaleCreate = Body(...)):
        try:
            if sale.quantity == 0:
                raise HTTPException(status_code=404, detail="No Quantity found")

            new_sale = Sales(**sale.dict())
            db.add(new_sale)
            db.commit()
            db.refresh(new_sale)

            response_data = jsonable_encoder(SaleResponse.model_validate(new_sale))

            return JSONResponse(
                status_code=201,
                content={
                    "message": "Sale created successfully",
                    "data": response_data
                }
            )

        except IntegrityError as e:
            db.rollback()
            error_message = str(e.orig)
            if "foreign key constraint" in error_message or "violates foreign key constraint" in error_message:
                if "product_id" in error_message:
                    raise HTTPException(status_code=400, detail="Product does not exist")

            match = re.search(r"Key \((.*?)\)=\(", error_message)
            if match:
                field = match.group(1)
                raise HTTPException(status_code=400, detail=f"{field.capitalize()} already exists")

            raise HTTPException(status_code=400, detail="Database integrity error")

        except HTTPException as e:
            return JSONResponse(status_code=e.status_code, content={"error": e.detail})

        except Exception as e:
            return JSONResponse(status_code=500, content={"error": str(e)})