from fastapi import FastAPI, HTTPException, Request, Depends
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
import crud
from crud import *
from jose import jwt
import hashlib
from typing import List

# pip install "python-jose[cryptography]"
# pip install "passlib[bcrypt]"


SECRET_KEY = "033d4faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"

#fonction utiles:
def hasher_mdp(mdp:str) -> str:                         # to block from getting back and retrieve the password (for security reasons for not to steal passwords)
    return hashlib.sha256(mdp.encode()).hexdigest()     # hexdigest : que pour des alphanumérique

def decoder_token(token:str)->dict:
    return jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)

def verifier_token(req: Request):
    token = req.headers["Authorization"]


# Classes contenu
class UserRegister(BaseModel):
    nom:str
    email:str
    mdp:str

class UserLogin(BaseModel):
    email:str
    mdp:str
    
class Operation(BaseModel):
    user_id: int
    action_id: int
    prix_achat: int
    date_achat: str

class Action(BaseModel):
    entreprise: int
    prix: int

class Vente(BaseModel):
    id: int
    date_vente: str
    prix_vente: int
    
######################################################""    
app = FastAPI()
#########################################################
# Début des endpoints

@app.get("/")
async def root():
    return {"message": "Hello World"}
###################################################
@app.post("/api/auth/inscription")
async def inscription(user:UserRegister):
    if len(crud.recup_user_avec_mail(user.email)) > 0:
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
####################################################""   
@app.post("/api/auth/token")
async def login_token(user:UserLogin):
    resultat = crud.recup_jeton_w_mail_mdp(user.email, hasher_mdp(user.mdp))
    if resultat is None:
        raise HTTPException(status_code=401, detail="Login ou mot de passe invalide")
    else:
        return {"token":resultat[0]}
################################################

# @app.get("/test")
# async def test():
#     return {"message": "Test"}

# @app.get("/suivre")
# async def test():
#     liste = [ i for i in range(100) if i%5==0]
#     return {"liste des multiples de 5": liste}

@app.post("/carnet_operations/")
async def creer_carnet_operations(op: Operation):
    connexion=sqlite3.connect('bdd.db')
    curseur= connexion.cursor()
    
    curseur.execute("""
                     INSERT INTO carnet_operation
                        VALUES ( NULL,?, ?, ?, ?, NULL, NULL)   
                    """, (op.user_id, op.action_id, op.prix_achat, op.date_achat))
    
    connexion.commit()
    connexion.close()
    
    return {"message": "Carnet d'operations created successfully!"}
#########################################################################"
@app.get("/actions/")
async def get_actions() -> List[dict]:
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()

    curseur.execute("""
                    SELECT * 
                    FROM action
                    """)

    actions = []
    for action in curseur.fetchall():
        actions.append({
            "id": action[0],
            "entreprise": action[1],
            "prix": action[2]
        })
    connexion.close()

    return actions
#####################################################
@app.get("/mesactions/")
# async def get_mes_actions(monid:int):
#     mes_actions = recup_sesactions(id)
#     return mes_actions
async def ses_actions(req: Request):
    try:
        mon_id= recup_id_w_jeton(req.headers["Authorization"])[0][0]
        return recup_sesactions(mon_id)
    except:
        raise HTTPException(status_code=401, detail="Vous devez être identifiés pour accéder à cet endpoint") 
###################################################################
@app.put("/vente/")
async def update_vente(vente: Vente):
    connexion=sqlite3.connect('bdd.db')
    curseur= connexion.cursor()
    
    curseur.execute("""
                    UPDATE carnet_operation
                        SET date_vente= ?,
                            prix_vente= ?
                        WHERE id= ?
                 
                        """, (vente.date_vente, vente.prix_vente, vente.id))
    
    connexion.commit()
    connexion.close()
    
    return {"message": "Vente created successfully!"}