from fastapi import APIRouter
from api.controller.user_endpoints import user_router

api = APIRouter()

api.include_router(router=user_router, prefix='/users', tags=['users'])

