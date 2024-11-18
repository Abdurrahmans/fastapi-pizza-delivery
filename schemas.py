from pydantic import BaseModel
from typing import  Optional



class SignUpModel(BaseModel):
    id:Optional[int]
    username:str
    email:str
    password:str
    is_staff:Optional[bool]
    is_active:Optional[bool]


    class Config:
        orm:True
        schema_extra={
            'example':{
                'username':'abdur',
                'email':'abdur@gmail.com',
                'password':'passward',
                'is_staff':False,
                'is_activ':True
            }


        }
