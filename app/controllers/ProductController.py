import re
from fastapi import Depends, Body, HTTPException, Path
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import IntegrityError

from app.db.session import get_db
from app.models.Product import Products
from app.schemas.product import ProductCreate, ProductResponse
from app.utils.decoraters.expose_routes import expose_route


class ProductController:

    @expose_route()
    def get_products(self, db: Session = Depends(get_db)):
        try:
            AllProduct = db.query(Products).all()

            if not AllProduct:
                raise HTTPException(status_code=404, detail="Product not found")

            products_data = jsonable_encoder(
                [ProductResponse.model_validate(p) for p in AllProduct]
            )

            return JSONResponse(
                status_code=200,
                content={
                    "message": "Products Fetched Successfully",
                    "data": products_data
                }
            )


        except HTTPException as e:
            return JSONResponse(status_code=e.status_code, content={"error": e.detail})

        except Exception as e:
            return JSONResponse(status_code=500, content={"error": str(e)})

    @expose_route()
    def get_product(self, db: Session = Depends(get_db), id: int = Path(...)):
        try:

            product = db.query(Products).filter(Products.id == id).first()

            if not product:
                raise HTTPException(status_code=404, detail="Product not found")

            product_data = ProductResponse.model_validate(product)
            response_data = jsonable_encoder(product_data)
            return JSONResponse(
                status_code=200,
                content={
                    "message": "Product Fetched Successfully",
                    "data": response_data
                }
            )

        except HTTPException as e:
            return JSONResponse(status_code=e.status_code, content={"error": e.detail})

        except Exception as e:
            return JSONResponse(status_code=500, content={"error": str(e)})

    @expose_route()
    def post_create_product(self, db: Session = Depends(get_db), product: ProductCreate = Body(...)):
        try:
            NewProduct = Products(**product.dict())
            db.add(NewProduct)
            db.commit()
            db.refresh(NewProduct)

            product_response = ProductResponse.model_validate(NewProduct)
            response_data = jsonable_encoder(product_response)

            return JSONResponse(
                status_code=200,
                content={
                    "message": "Product Created Successfully",
                    "data": response_data
                }
            )

        except IntegrityError as e:
            db.rollback()
            error_message = str(e.orig)
            if "foreign key constraint" in error_message or "violates foreign key constraint" in error_message:
                if "category_id" in error_message:
                    raise HTTPException(status_code=400, detail="Category does not exist")

            match = re.search(r"Key \((.*?)\)=\(", error_message)
            if match:
                field = match.group(1)
                raise HTTPException(status_code=400, detail=f"{field.capitalize()} already exists")

            raise HTTPException(status_code=400, detail="Database integrity error")

        except HTTPException as e:
            return JSONResponse(status_code=e.status_code, content={"error": e.detail})

        except Exception as e:
            return JSONResponse(status_code=500, content={"error": str(e)})