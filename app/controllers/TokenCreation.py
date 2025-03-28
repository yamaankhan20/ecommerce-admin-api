from app.utils.decoraters.expose_routes import expose_route
import httpx
from fastapi.responses import JSONResponse

class TokenController:

    # @expose_route()
    def post_create_demon(self):
        try:
            data = {
             "creator": "zig1l6wk5s3mrx34zpstmvfnp3spjcn42tmzpas33a",
             "subDenom": "Freya",
             "symbol": "fr",
             "description": "Qui velit cumque vel",
             "maxSupply": "1000000000",
             "canChangeMaxSupply": True,
             "URI": "https://plum-accepted-dolphin-229.mypinata.cloud/ipfs/Qme71eMxJMBm9VVSxvRkt7ytXr1yAzat1QqBsULsURg6oi",
             "URIHash": "c05348f17c6d62fa6b91598fb1e14942fa41eb451564329e92577c3d5d6c889a",
            }
            response = httpx.post("https://testnet-api.zigchain.com/zigchain.factory.Msg/CreateDenom", json=data)  # example API

            if response.status_code != 200:
                return JSONResponse(
                    status_code=response.status_code,
                    content={"error": response.text}
                )

            return JSONResponse(
                status_code=200,
                content={
                    "message": "CreateDenom success",
                    "response": response.json()
                }
            )

        except Exception as e:
            return JSONResponse(status_code=500, content={"error": str(e)})