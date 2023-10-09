from fastapi import APIRouter, HTTPException
from models.models import Hash_algorithm
import hashlib
from hmac import compare_digest

router = APIRouter()

@router.get("/hash/compare/algorithm/{algorithmStr}/value/{valueStr}/hash/{hashStr}", summary="Compare Hash", description="Return True if the hash is equal to the value hashed using the algorithm selected otherwise return False")
def Hash_compare(algorithmStr: Hash_algorithm,valueStr:str,hashStr:str):
    try:
        h=hashlib.new(algorithmStr.name)
        h.update(valueStr.encode())
        processed_data = compare_digest(h.hexdigest(),hashStr)

        response_data = {
            "status": "success",
            "data": {
                "processed_data": processed_data,
                "additional_info": ""
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail="Ocurrió un error en el procesamiento de datos.")
    return response_data

@router.get("/hash/compare/algorithm/{algorithmStr}/salt/{saltStr}value/{valueStr}/hash/{hashStr}", summary="Compare Hash adding salt", description="Return True if the hash is equal to the value hashed using the algorithm selected and adding salt otherwise return False")
def Hash_compare_salt(algorithmStr: Hash_algorithm,saltStr:str,valueStr:str,hashStr:str):
    try:
        h=hashlib.new(algorithmStr.name)
        salted=saltStr+valueStr
        h.update(salted.encode())
        processed_data = compare_digest(h.hexdigest(),hashStr)

        response_data = {
            "status": "success",
            "data": {
                "processed_data": processed_data,
                "additional_info": ""
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail="Ocurrió un error en el procesamiento de datos.")
    return response_data


@router.get("/hash/compare/algorithm/{algorithmStr}/pepper/{pepperStr}value/{valueStr}/hash/{hashStr}", summary="Compare Hash adding pepper", description="Return True if the hash is equal to the value hashed using the algorithm selected and adding pepper otherwise return False")
def Hash_compare_pepper(algorithmStr: Hash_algorithm,valueStr:str,pepperStr:str,hashStr:str):
    try:
        h=hashlib.new(algorithmStr.name)
        peppered=valueStr+pepperStr
        h.update(peppered.encode())
        processed_data = compare_digest(h.hexdigest(),hashStr)

        response_data = {
            "status": "success",
            "data": {
                "processed_data": processed_data,
                "additional_info": ""
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail="Ocurrió un error en el procesamiento de datos.")
    return response_data