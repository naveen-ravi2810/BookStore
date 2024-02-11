from fastapi import APIRouter, Depends
from core.security import JWTBearer
from db import SessionDep
from curd.address_curd import get_address_by_email, add_address_by_email
from models.address_model import AddressCreate, AddressShow
from typing import List
router = APIRouter()


@router.get("",response_model=List[AddressShow])
def get_address(session: SessionDep, user_data=Depends(JWTBearer())):
    addresses = get_address_by_email(email=user_data['identity'],session=session)
    return addresses


@router.post("")
def add_address(session: SessionDep, address:AddressCreate, user_data=Depends(JWTBearer())):
    add_address_by_email(address_details=address, session=session, email=user_data['identity'])
    return {"2":address}


