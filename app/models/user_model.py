
from app.exc.bad_request import BadRequestError

from app.exc.email_already_used import EmailAlreadyUsedError
from app.services.handler_json import reading_json, writing_json
from app.services.email_already_used import email_already_used
class User:
    def __init__ (self, nome, email):
        self.nome = nome
        self.email = email
        self.id = self.dinamic_id()

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
            self.email = self.email.lower()
    
    @staticmethod
    def get_users():
        return reading_json()     
    
    

