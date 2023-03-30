from fastapi import APIRouter, status, Depends, HTTPException, Response
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from models.user_model import UserModel
from core.dependencies import get_session
from references.user_reference import UserUpdateSchema

#####BYPASS WARNING SQLMODEL SELECT####

from sqlmodel.sql.expression import select, SelectOfScalar

SelectOfScalar.inherit_cache = True #type: ignore
select.inherit_cache = True #type: ignore

####END BYPASS####

user_router = APIRouter()

#POST
@user_router.post('/', status_code=status.HTTP_201_CREATED, response_model=UserModel)
async def post_user(user: UserModel, db: AsyncSession = Depends(get_session)) -> Response:
    
    new_user = UserModel(fullname=user.fullname, email=user.email, password=user.password)
    db.add(new_user)
    await db.commit()
    
    return new_user


#GET ALL
@user_router.get('/', status_code=status.HTTP_200_OK, response_model=List[UserModel])
async def get_all_users(db: AsyncSession = Depends(get_session)) -> Response:
    
    async with db as session:
        query_result = await session.execute(select(UserModel))
        all_users: List[UserModel] = query_result.scalars().all()
        
        return all_users


#GET BY ID
@user_router.get('/{id}', status_code=status.HTTP_200_OK, response_model=UserModel)
async def get_by_id(id: int, db: AsyncSession = Depends(get_session)) -> Response:
    
    async with db as session:
        query_result = await session.execute(select(UserModel).filter(UserModel.id == id))
        user = query_result.scalar()
        
        if query_result is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Usuário não encontrado')
        else:
            return user


#UPDATE
@user_router.patch('/{id}', status_code=status.HTTP_200_OK, response_model=UserModel)
async def update_user(id: int, data: UserUpdateSchema, db: AsyncSession = Depends(get_session)) -> Response:
    
    async with db as session:
        query_result = await session.execute(select(UserModel).filter(UserModel.id == id))
        user = query_result.scalar()
        
        if query_result is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Usuário não encontrado')
        else:
            
            for key, value in data.dict(exclude_unset=True).items():
                setattr(user, key, value)
            
            await db.commit()
            return user


#DELETE
@user_router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT, response_model=UserModel)
async def delete_user(id: int, db: AsyncSession = Depends(get_session)):
    
    async with db as session:
        query_result = await session.execute(select(UserModel).filter(UserModel.id == id))
        user_to_delete = query_result.scalar()
        
        if query_result is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Usuário não encontrado')
        else:
            await db.delete(user_to_delete)
            await db.commit()

