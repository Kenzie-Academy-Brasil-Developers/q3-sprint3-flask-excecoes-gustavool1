from http import HTTPStatus
from flask import Flask,request

from app.exc.bad_request import BadRequestError
from app.exc.email_already_used import EmailAlreadyUsedError
from app.services.handler_json import reading_json, writing_json
from app.services.isnt_string import inst_string
from app.models.user_model import User 
app = Flask(__name__)

@app.get("/user")
def retrieve():
    return User.get_users(), HTTPStatus.OK


@app.post("/user")
def creating_user_route():

    data = request.get_json()
    user = User(**data)
    try:
        user.save_user(user)
        writing_json(user.__dict__)
        return user.__dict__, HTTPStatus.CREATED
        
    except EmailAlreadyUsedError:
        return {"error":"User already exists."}, HTTPStatus.CONFLICT
    
    except BadRequestError:
        return inst_string(user.nome, user.email), HTTPStatus.BAD_REQUEST
        
