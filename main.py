from fastapi import FastAPI, HTTPException, Request, Depends
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
import crud
from jose import jwt
import hashlib




SECRET_KEY = "033d4faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"

def hasher_mdp(mdp:str) -> str:
    return hashlib.sha256(mdp.encode()).hexdigest()

def decoder_token(token:str)->dict:
    return jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)

def verifier_token(req: Request):
    token = req.headers["Authorization"]



class UserRegister(BaseModel):
    nom:str
    email:str
    mdp:str

class UserLogin(BaseModel):
    email:str
    mdp:str
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/api/auth/inscription")
async def inscription(user:UserRegister):
    if len(crud.get_users_by_mail(user.email)) > 0:
        raise HTTPException(status_code=403, detail="L'email fourni possède déjà un compte")
    else:
        id_user = crud.creer_utilisateur(user.nom, user.email, hasher_mdp(user.mdp), None)
        token = jwt.encode({
            "email" : user.email,
            "mdp" : user.mdp,
            "id" : id_user
        }, SECRET_KEY, algorithm=ALGORITHM)
        crud.update_token(id_user, token)
        return {"token" : token}
    
@app.post("/api/auth/token")
async def login_token(user:UserLogin):
    resultat = crud.obtenir_jwt_depuis_email_mdp(user.email, hasher_mdp(user.mdp))
    if resultat is None:
        raise HTTPException(status_code=401, detail="Login ou mot de passe invalide")
    else:
        return {"token":resultat[0]}


@app.get("/test")
async def test():
    return {"message": "Test"}

@app.get("/suivre")
async def test():
    liste = [ i for i in range(100) if i%5==0]
    return {"liste des multiples de 5": liste}