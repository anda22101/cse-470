
from fastapi import Request





def set_user_session(request: Request, email: str):
    request.session['email'] = email

def get_user_session(request: Request) -> str | None:
    return request.session.get("email")

def clear_user_session(request: Request):
    request.session.pop("email", None)

def is_logged_in(request: Request) -> bool:
    return "email" in request.session