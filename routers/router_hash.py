
from fastapi import APIRouter, HTTPException
from models.models import Hash_algorithm
import hashlib

router = APIRouter()

@router.get("/hash/algorithm/{algorithmStr}/value/{valueStr}", summary="Hash", description="Return the Hash, of the value provided using the hash algorithm selected")
def Hash_value(algorithmStr: Hash_algorithm,valueStr:str):
    try:
        h=hashlib.new(algorithmStr.name)
        h.update(valueStr.encode())
        processed_data = h.hexdigest()  

        response_data = {
            "status": "success",
            "data": {
                "processed_data": processed_data,
                "additional_info": f"Hash using {algorithmStr.name}"
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail="Ocurrió un error en el procesamiento de datos.")
    return response_data

@router.get("/hash/algorithm/{algorithmStr}/value/{valueStr}/salt/{saltStr}", summary="Hash adding salt", description="Return the Hash, of the value provided using the hash algorithm selected and adding salt before hasing")
def Hash_value_salt(algorithmStr: Hash_algorithm,saltStr:str,valueStr:str):
    try:
        h=hashlib.new(algorithmStr.name)
        salted=saltStr+valueStr
        print(salted)
        h.update(salted.encode())
        processed_data = h.hexdigest()  

        response_data = {
            "status": "success",
            "data": {
                "processed_data": processed_data,
                "additional_info": f"Hash using {algorithmStr.name} and salt"
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail="Ocurrió un error en el procesamiento de datos.")
    return response_data

@router.get("/hash/algorithm/{algorithmStr}/value/{valueStr}/pepper/{pepperStr}", summary="Hash adding pepper", description="Return the Hash, of the value provided using the hash algorithm selected and adding peper after hasing")
def Hash_value_pepper(algorithmStr: Hash_algorithm,valueStr:str,pepperStr:str):
    try:
        h=hashlib.new(algorithmStr.name)
        peppered=valueStr+pepperStr
        h.update(peppered.encode())
        processed_data = h.hexdigest()  

        response_data = {
            "status": "success",
            "data": {
                "processed_data": processed_data,
                "additional_info": f"Hash using {algorithmStr.name} and pepper"
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail="Ocurrió un error en el procesamiento de datos.")
    return response_data