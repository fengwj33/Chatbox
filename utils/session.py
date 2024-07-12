from uuid import uuid4
from fastapi import Depends, Request, Response

session_list = {}

def session():
    def process_cookie(request: Request, response:Response):
        global session_list
        session_key = request.cookies.get('sessionKey')
        if not session_key:
            session_key = uuid4()
            response.set_cookie('sessionKey', session_key)
        session_list.setdefault(session_key,{})
        return session_list[session_key]
    return Depends(process_cookie)