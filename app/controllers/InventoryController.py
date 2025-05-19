from fastapi import Depends, HTTPException, Path
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from app.db.session import get_db
from app.models.Inventory import Inventory
from app.schemas.inventory import InventoryResponse, InventoryUpdate
from app.utils.decoraters.expose_routes import expose_route

class InventoryController:

    @expose_route()
    def get_inventory(self, db: Session = Depends(get_db)):
        try:
            inventory = db.query(Inventory).all()
            if not inventory:
                raise HTTPException(status_code=404, detail="No inventory records found")

            response_data = jsonable_encoder([
                InventoryResponse.model_validate(i) for i in inventory
            ])

            return JSONResponse(
                status_code=200,
                content={
                    "message": "Inventory retrieved successfully",
                    "data": response_data
                }
            )

        except HTTPException as e:
            return JSONResponse(status_code=e.status_code, content={"error": e.detail})
        except Exception as e:
            return JSONResponse(status_code=500, content={"error": str(e)})

    @expose_route()
    def put_inventory(
        self,
        product_id: int = Path(...),
        update_data: InventoryUpdate = Depends(),
        db: Session = Depends(get_db)
    ):
        try:
            item = db.query(Inventory).filter(Inventory.product_id == product_id).first()
            if not item:
                raise HTTPException(status_code=404, detail="Inventory item not found")

            item.stock_level = update_data.stock_level
            db.commit()
            db.refresh(item)

            response_data = jsonable_encoder(InventoryResponse.model_validate(item))

            return JSONResponse(
                status_code=200,
                content={
                    "message": "Inventory updated successfully",
                    "data": response_data
                }
            )

        except HTTPException as e:
            return JSONResponse(status_code=e.status_code, content={"error": e.detail})
        except Exception as e:
            return JSONResponse(status_code=500, content={"error": str(e)})

    @expose_route()
    def get_low_stock_inventory(self, db: Session = Depends(get_db)):
        try:
            items = db.query(Inventory).filter(Inventory.stock_level <= 5).all()
            if not items:
                raise HTTPException(status_code=404, detail="No low-stock products found")

            response_data = jsonable_encoder([
                InventoryResponse.model_validate(i) for i in items
            ])

            return JSONResponse(
                status_code=200,
                content={
                    "message": "Low-stock products retrieved successfully",
                    "data": response_data
                }
            )

        except HTTPException as e:
            return JSONResponse(status_code=e.status_code, content={"error": e.detail})
        except Exception as e:
            return JSONResponse(status_code=500, content={"error": str(e)})
