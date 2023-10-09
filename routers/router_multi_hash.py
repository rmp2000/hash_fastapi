from fastapi import APIRouter, HTTPException, UploadFile
from models.models import Hash_algorithm, RequestData
import hashlib

router = APIRouter()

@router.put("/hash/multiple/algorithm/{algorithmStr}", summary="Hash multiple values", description="Return a list of hash using the algorithm selected")
def Hash_multiple(algorithmStr: Hash_algorithm,list_hash:RequestData):
    try:
        final_list=[]
        for item in list_hash.input_data:
            h=hashlib.new(algorithmStr.name)
            h.update(item.encode())
            final_list.append(h.hexdigest())
        processed_data = final_list  

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

@router.put("/hash/multiple/algorithm/{algorithmStr}/salt/{saltStr}", summary="Hash adding salt multiple values", description="Return a list of hash using the algorithm selected adding salt before hasing")
def Hash_multiple_salt(algorithmStr: Hash_algorithm,saltStr:str,list_hash:RequestData): 
    try:
        final_list=[]
        for item in list_hash.input_data:
            h=hashlib.new(algorithmStr.name)
            salted=saltStr+item
            print(salted)
            h.update(salted.encode())
            final_list.append(h.hexdigest())

        processed_data = final_list  

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

@router.put("/hash/multiple/algorithm/{algorithmStr}/pepper/{pepperStr}", summary="Hash adding pepper multiple values", description="Return a list of hash using the algorithm selected and adding pepper after hasing")
def Hash_multiple_pepper(algorithmStr: Hash_algorithm,list_hash:RequestData,pepperStr:str):
    try:
        final_list=[]
        for item in list_hash.input_data:
            h=hashlib.new(algorithmStr.name)
            peppered=item+pepperStr
            h.update(peppered.encode())
            final_list.append(h.hexdigest())
        processed_data = final_list 

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

@router.post("/hash/multiple/file/algorithm/{algorithmStr}",summary="Hash File",description="Return the hash of the File provided using the algorithm selected")
async def Hash_file(algorithmStr: Hash_algorithm,file_updated: UploadFile=(...)):
    try:
        h=hashlib.new(algorithmStr.name)
        for chunk in iter(lambda: file_updated.file.read(65536), b''):
            h.update(chunk)
        processed_data = h.hexdigest()  

        response_data = {
            "status": "success",
            "data": {
                "processed_data": processed_data,
                "additional_info": f"Hash a file using {algorithmStr.name}"
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail="Ocurrió un error en el procesamiento de datos.")
    return response_data
