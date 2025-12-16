from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from main import get_db
from models import Data

router = APIRouter()

@router.get('/')
async def get_data(db: Session = Depends(get_db)):
    #... rest of the get data endpoint code...

@router.post('/')
async def create_data(data: Data, db: Session = Depends(get_db)):
    #... rest of the create data endpoint code...

@router.put('/{data_id}')
async def update_data(data_id: int, data: Data, db: Session = Depends(get_db)):
    #... rest of the update data endpoint code...

@router.delete('/{data_id}')
async def delete_data(data_id: int, db: Session = Depends(get_db)):
    #... rest of the delete data endpoint code...
