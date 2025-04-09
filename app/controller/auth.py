from fastapi import APIRouter, Depends, HTTPException, Request, status, Form
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from ..models import user_model
from ..database import get_db
from ..session import *

router = APIRouter(tags=['Authentication'])

@router.post('/login')
async def login(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    db: AsyncSession = Depends(get_db)
):
    
    
    result = await db.execute(select(user_model.User).where(user_model.User.email == email))
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    
    if user.password != password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password")

    set_user_session(request, email)
    return {"message": "Login successful"}