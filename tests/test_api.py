import os
import requests

Endpoint="http://127.0.0.1:8000"

def test_can_call_endpoint():
    response = requests.get(Endpoint)
    assert response.status_code==200

def test_base():
    algorithmStr="sha256"
    valueStr="test"
    response = requests.get(Endpoint+f"/hash/algorithm/{algorithmStr}/value/{valueStr}")
    assert response.status_code==200
    test_data=response.json()
    assert test_data["data"]["processed_data"]=="9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"

def test_base_salt():
    algorithmStr="sha256"
    valueStr="test"
    saltStr="salt"
    response = requests.get(Endpoint+f"/hash/algorithm/{algorithmStr}/value/{valueStr}/salt/{saltStr}")
    assert response.status_code==200
    test_data=response.json()
    assert test_data["data"]["processed_data"]=="1bc1a361f17092bc7af4b2f82bf9194ea9ee2ca49eb2e53e39f555bc1eeaed74"

def test_base_pepper():
    algorithmStr="sha256"
    valueStr="test"
    pepperStr="pepper"
    response = requests.get(Endpoint+f"/hash/algorithm/{algorithmStr}/value/{valueStr}/pepper/{pepperStr}")
    assert response.status_code==200
    test_data=response.json()
    assert test_data["data"]["processed_data"]=="217cce063ef417152ebf87aa9c3348f8c452b48e07609231ed2f72978cb18597"

def test_multi():
    payload={"input_data": [
    "test",
    "this is a test"
    ]
    }
    algorithmStr="md5"
    response= requests.put(Endpoint+f"/hash/multiple/algorithm/{algorithmStr}",json=payload)
    assert response.status_code==200
    test_data=response.json()
    assert test_data["data"]["processed_data"][0]=="098f6bcd4621d373cade4e832627b4f6"
    assert test_data["data"]["processed_data"][1]=="54b0c58c7ce9f2a8b551351102ee0938"
    data= response.json()

def test_multi_salt():
    payload={"input_data": [
    "test",
    "this is a test"
    ]
    }
    algorithmStr="sha256"
    saltStr="salt"
    response= requests.put(Endpoint+f"/hash/multiple/algorithm/{algorithmStr}/salt/{saltStr}",json=payload)
    assert response.status_code==200
    test_data=response.json()
    print(test_data)
    assert test_data["data"]["processed_data"][0]=="1bc1a361f17092bc7af4b2f82bf9194ea9ee2ca49eb2e53e39f555bc1eeaed74"
    assert test_data["data"]["processed_data"][1]=="a9fdb1deeb5050e0bc2eb69afd4c41258ce57a3a619f1424175986ad5dd2378a"

    data= response.json()

def test_multi_pepper():
    payload={"input_data": [
    "test",
    "this is a test"
    ]
    }
    algorithmStr="sha256"
    pepperStr="pepper"
    response= requests.put(Endpoint+f"/hash/multiple/algorithm/{algorithmStr}/pepper/{pepperStr}",json=payload)
    assert response.status_code==200
    test_data=response.json()
    print(test_data)
    assert test_data["data"]["processed_data"][0]=="217cce063ef417152ebf87aa9c3348f8c452b48e07609231ed2f72978cb18597"
    assert test_data["data"]["processed_data"][1]=="2688358d1e4397e9717c520a3dd1e33ea782982a41059ea6f1c40786b89b7ea4"

    data= response.json()

def test_comparar():
    algorithmStr="sha256"
    valueStr="test"
    hashStr="9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"
    response = requests.get(Endpoint+f"/hash/compare/algorithm/{algorithmStr}/value/{valueStr}/hash/{hashStr}")
    assert response.status_code==200
    test_data=response.json()
    assert test_data["data"]["processed_data"]==True
    hashStr="Nohash"
    response = requests.get(Endpoint+f"/hash/compare/algorithm/{algorithmStr}/value/{valueStr}/hash/{hashStr}")
    assert response.status_code==200
    test_data=response.json()
    assert test_data["data"]["processed_data"]==False

def test_comparar_salt():
    algorithmStr="sha256"
    valueStr="test"
    saltStr="salt"
    hashStr="1bc1a361f17092bc7af4b2f82bf9194ea9ee2ca49eb2e53e39f555bc1eeaed74"
    response = requests.get(Endpoint+f"/hash/compare/algorithm/{algorithmStr}/salt/{saltStr}value/{valueStr}/hash/{hashStr}")
    assert response.status_code==200
    test_data=response.json()
    assert test_data["data"]["processed_data"]==True
    hashStr="Nohash"
    response = requests.get(Endpoint+f"/hash/compare/algorithm/{algorithmStr}/salt/{saltStr}value/{valueStr}/hash/{hashStr}")
    assert response.status_code==200
    test_data=response.json()
    assert test_data["data"]["processed_data"]==False

def test_comparar_pepper():
    algorithmStr="sha256"
    valueStr="test"
    pepperStr="pepper"
    hashStr="217cce063ef417152ebf87aa9c3348f8c452b48e07609231ed2f72978cb18597"
    response = requests.get(Endpoint+f"/hash/compare/algorithm/{algorithmStr}/pepper/{pepperStr}value/{valueStr}/hash/{hashStr}")
    assert response.status_code==200
    test_data=response.json()
    assert test_data["data"]["processed_data"]==True
    hashStr="Nohash"
    response = requests.get(Endpoint+f"/hash/compare/algorithm/{algorithmStr}/pepper/{pepperStr}value/{valueStr}/hash/{hashStr}")
    assert response.status_code==200
    test_data=response.json()
    assert test_data["data"]["processed_data"]==False

def test_file():
    algorithmStr="blake2b"
    file_path = os.path.join(os.path.dirname(__file__), "test.txt")
    url = Endpoint+f"/hash/multiple/file/algorithm/{algorithmStr}"
    with open(file_path, "rb") as test_file:
            files = {"file_updated": test_file}
            response = requests.post(url, files=files)
    assert response.status_code==200
    test_data=response.json()
    assert test_data["data"]["processed_data"]=="06a186d5f497d036488e4b8fae4e8662ca72f57a199efc4c7eb1a57a7dc838af49fc5de54647201c40d2280e38142a36f4bdf955ae4994292b63c15b1d98c3b9"