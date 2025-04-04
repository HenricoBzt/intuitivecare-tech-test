from app.backend.database import get_session
from app.backend.models import OperadorasModel
from app.backend.schemas import OperadoraList

from fastapi import APIRouter, HTTPException, Depends, Query

from http import HTTPStatus
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from typing import Annotated, Optional

T_AssyncSession = Annotated[AsyncSession, Depends(get_session)]
T_query = Annotated[Optional[str], Query(min_length=None, description='Termo para busca nas operadoras')]

router = APIRouter(
    prefix="/operadoras",
    tags=['Operadoras']
    )

@router.get('/search/', response_model=OperadoraList)
async def search_operadoras(
    session: T_AssyncSession,
    query:  T_query = None,
    skip: int = 0,
    limit: int = 10,
    ):

    stmt_base = select(OperadorasModel).order_by(OperadorasModel.nome_fantasia)
    stmt_query = stmt_base

    if query:
        stmt_query = stmt_base.where(OperadorasModel.nome_fantasia.ilike(f'%{query}%') | 
                          OperadorasModel.razao_social.ilike(f'%{query}%'))
        
    stmt_pagined = stmt_query.offset(skip).limit(limit)

    result = await session.execute(stmt_pagined)
    operadoras = result.scalars().all()

    if not operadoras:
        raise HTTPException(
            status_code= HTTPStatus.NOT_FOUND,
            detail='Nenhuma operadora encontrada')

    return {'results': operadoras} 
    




    


