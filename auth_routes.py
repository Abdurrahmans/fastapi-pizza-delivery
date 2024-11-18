from fastapi import APIRouter,status
from database import Session,engine
from schemas import SignUpModel
from models import User
from fastapi.exceptions import HTTPException
from werkzeug.security import generate_password_hash


auth_router = APIRouter(
    prefix="/auth",
    tags=['auth']
)

session =Session(bind=engine)

@auth_router.get('/')
async def hello():
    return{'message':'hello world'}



@auth_router.post('/signup')
async def signup(user:SignUpModel):
    db_email = session.query(User).filter(User.email== user.email).first()

    if db_email is not None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='User with the eamil already Exists')
    
    db_username = session.query(User).filter(User.username== user.username).first()
    if db_username is not None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail='User with the user already Exists')
    

    new_user = User(
        username=user.username,
        email = user.email,
        password = generate_password_hash(user.password),
        is_staff = user.is_staff,
        is_active = user.is_active

    )

    session.add(new_user)
    session.commit()

    return new_user
    




