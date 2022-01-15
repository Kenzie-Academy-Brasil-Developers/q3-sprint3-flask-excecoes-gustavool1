from json import dump
from app.exc.bad_request import BadRequestError

from app.exc.email_already_used import EmailAlreadyUsedError
from app.services.handler_json import reading_json, writing_json
from app.services.email_already_used import email_already_used
class User:
    def __init__ (self, nome, email):
        self.nome = nome
        self.email = email
        self.id = self.dinamic_id()


    def __repr__(self) -> str:
        return f"Nome:{self.nome} | Email:{self.email} | Id:{self.id}"


    def __str__(self, atribute) -> str:
        return f"{self.atribute}"


    def is_string(self):
        obj = {}
        if type(self.nome) != str:
            obj["name"] = type(self.nome).__name__
        if type(self.email) != str:
            obj["email"] = type(self.email).__name__
        
        return obj


    def dinamic_id(self):
        users_list = self.get_users()
        return len(users_list.get("data")) + 1 


    def save_user(self,user):
        if email_already_used(user.email):
            raise EmailAlreadyUsedError
            ...
        if not type(self.email) == str or not type(self.nome) == str:

            raise BadRequestError
        else:
            self.nome = self.nome.title()
            self.email = self.email.upper()
    
    @staticmethod
    def get_users():
        return reading_json()     
    
    

