from enum import Enum
from typing import List
from pydantic import BaseModel, constr

class Hash_algorithm(str, Enum):
    md5 = "md5"
    sha1 = "sha1"
    sha224 = "sha224"
    sha256 = "sha256"
    sha384 = "sha384"
    sha512 = "sha512"
    sha3_224 = "sha3_224"
    sha3_256 = "sha3_256"
    sha3_384 = "sha3_384"
    sha3_512 = "sha3_512"
    blake2b = "blake2b"
    blake2s = "blake2s"

class RequestData(BaseModel):
    input_data: List[constr(min_length=1)]