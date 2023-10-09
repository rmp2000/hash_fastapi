from fastapi import FastAPI
from routers.router_hash import router as router_hash
from routers.router_compare_hash import router as router_compare
from routers.router_multi_hash import router as router_multi_hash

app=FastAPI(
    title="HASH API",
    description="Welcome to the Hash API. This API provides services for generating and comparing hashes for word lists, individual words, and files. Hashes are unique representations of the provided data that can be used to verify their integrity and compare them to other hashes.",
    )

@app.get("/")
async def Thanks():
    return {
            "status": "success",
            "data": {
                "processed_data": "Thanks for using this api, created to practice and learn abaout fast api",
                "additional_info": "The Creator : https://github.com/rmp2000"
            }
        }

app.include_router(router_hash,tags=["Hash"])
app.include_router(router_compare,tags=["Comparar Hash"])
app.include_router(router_multi_hash,tags=["Hash multiple"])