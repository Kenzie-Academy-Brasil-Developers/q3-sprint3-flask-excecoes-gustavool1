from app.exc.email_already_used import EmailAlreadyUsedError
from app.services.handler_json import reading_json
def email_already_used(email):
    users_list = reading_json()
    users_list = users_list["data"]

    for user in users_list:
        if type(email) == str:
            if user["email"] == email.lower():
                raise EmailAlreadyUsedError
    return False
