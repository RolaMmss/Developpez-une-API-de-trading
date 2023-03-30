


Class Utilisateur(BasedModel):
    nom:str
    email:str
    mdp:str
    jws:str    
    
    
    @app.get("/")
    async def creer utlisateur(nom: Utilisateur, email: Utilisateur, mdp:Utilisateur, jws:Utilisateur):
        
        
        
        return {"message": "Hello World"}


@app.get("/test")
async def test():
    # return {"message": "test"}
    liste= [ i for i in range (100) if i%5==0 ]
    return {"LISTE DE SMULTIPLES DE 5": liste}