import socketio

from fastapi import FastAPI
from typing import AnyStr, List
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from address_parser import address_parser, parse_address_list


# fast_app = FastAPI(
#     openapi_url='/api/notifications/openapi.json',
#     docs_url='/api/notifications/docs',
#     redoc_url='/api/notifications/redoc'
# )
# sio = socketio.AsyncServer(
#     async_mode='asgi',
#     cors_allowed_origins='*'
# )
# app = socketio.ASGIApp(
#     socketio_server=sio,
#     other_asgi_app=fast_app,
#     socketio_path='/api/notifications/socket.io/'
# )

app = FastAPI()


class AddressListRequest(BaseModel):
    address_list: List[str]


class SingleAddressRequest(BaseModel):
    address: str


class NameDetectRequest(BaseModel):
    name: str


class NameListDetectRequest(BaseModel):
    name: List[str]


@app.get('/', status_code=200)
async def root():
    return {"message": "Welcome to the Black Parade"}


@app.post('/parse_address_list', status_code=200)
async def parse_address(addresses: AddressListRequest):
    addresses = addresses.address_list

    parsed_result = parse_address_list(addresses)
    
    return {"result": parsed_result}

@app.post('/parse_single_address', status_code=200)
async def parse_single_address(address: SingleAddressRequest):
    address = address.address

    parsed_address = address_parser(address)

    return {"message": parsed_address}

@app.post('/detect_person_name', status_code=200)
async def detect_name(request: NameDetectRequest):
    name = request.name
    return {"name": name}