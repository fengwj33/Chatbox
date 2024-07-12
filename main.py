from fastapi import FastAPI

from utils.session import session

app = FastAPI()

@app.get("/")
def root(session:dict = session()):
    session.setdefault('msg', '')
    session['msg']+='a'
    return session

