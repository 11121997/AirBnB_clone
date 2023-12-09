#!/usr/bin/python3
'''class User module'''
from models.base_model import BaseModel


class User(BaseModel):
    """
    class User that inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
