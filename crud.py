import sqlite3



def creer_utilisateur(nom:str, email:str, mdp:str, cle_jwt:str) -> int: 
    connexion = sqlite3.connect("bdd.db")   #Se connecter à la base de données

    curseur = connexion.cursor() #SQL.sh pour apprender SQL

    curseur.execute(""" 
        INSERT INTO utilisateur 
            VALUES (NULL, ?, ?, 1, ?, ?)           
    """, (nom,email,mdp,cle_jwt))        # VALUES (NULL, 'Rola', 'rola@rola.com', 'azerty123')
    connexion.commit()

    connexion.close()




def creer_asso_suivi_suiveur(suivi:int, suiveur:int) -> None:
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()

    curseur.execute("""
                    INSERT INTO asso_suivi_suiveur 
                        VALUES ( ?, ?)   
                    """, (suivi, suiveur))
    connexion.commit()
# qd il y a points d'interrogation >>>il va chercher la valeur qui sera donnée plus tard)cf : .format()
    connexion.close()
    
    
    
def creer_carnet_operations(user_id:int, action_id:int, prix_achat:int, date_achat:str) -> None:
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()

    curseur.execute("""
                    INSERT INTO carnet_operation
                        VALUES ( NULL,?, ?, ?, ?, NULL, NULL)   
                    """, (user_id, action_id, prix_achat, date_achat))
    connexion.commit()
# qd il y a points d'interrogation >>>il va chercher la valeur qui sera donnée plus tard)cf : .format()
    connexion.close()



def inserer_vente_operations(id:int, date_vente:str, prix_vente:int)->None:
    connexion=sqlite3.connect('bdd.db')
    curseur= connexion.cursor()
    
    curseur.execute("""
                    UPDATE carnet_operation
                        SET date_vente= ?,
                            prix_vente= ?
                        WHERE id= ?
                 
                        """, (date_vente, prix_vente,id))
    
    connexion.commit()
    connexion.close()
    # curseur.execute("""
    #                 UPDATE playlist
    #                     SET nom = ?
    #                     WHERE id= ?
                 
    
def creer_action(entreprise:str, prix:int) -> None:
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()

    curseur.execute("""
                    INSERT INTO action 
                        VALUES (NULL, ?, ?)   
                    """, (entreprise, prix))
    connexion.commit()
# qd il y a points d'interrogation >>>il va chercher la valeur qui sera donnée plus tard)cf : .format()
    connexion.close()
    
def modifier_carnet_operations(user_id:int, action_id:int, prix_achat:int, date_achat:str, prix_vente:int, date_vente:str) -> None:
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()

    curseur.execute("""
                    UPDATE carnet_opreation
                        VALUES ( NULL,?, ?, ?, ?, ?, ?)   
                    """, (user_id, action_id, prix_achat, date_achat, prix_vente, date_vente))
    connexion.commit()
# qd il y a points d'interrogation >>>il va chercher la valeur qui sera donnée plus tard)cf : .format()
    connexion.close()
 
 #### trouver id à partir mail####
 
def recup_id_avec_mail(email:str):
    connexion=sqlite3.connect('bdd.db')
    curseur= connexion.cursor()
        
    curseur.execute("""
                        SELECT id
                        FROM utilisateur
                        WHERE email= ?
                        """, (email,))
    rslt=curseur.fetchall()
    return rslt
                                        ####trouver jeton à partir login/mdp   ####

def recup_jeton_w_mail_mdp(email:str, mdp:str ):
    connexion=sqlite3.connect('bdd.db')
    curseur= connexion.cursor()
        
    curseur.execute("""
                        SELECT cle_jwt
                        FROM utilisateur
                        WHERE email= ?
                        AND   mdp=?
                        """, (email, mdp))
    rslt=curseur.fetchall()
    return rslt

                                ### trouver id à partir jeton  ####

def recup_id_w_jeton(cle_jwt:str ):
    connexion=sqlite3.connect('bdd.db')
    curseur= connexion.cursor()
        
    curseur.execute("""
                        SELECT id
                        FROM utilisateur
                        WHERE cle_jwt= ?
                        """, (cle_jwt,))
    rslt=curseur.fetchall()
    return rslt




def delete_user(email:str) ->None:
    connexion=sqlite3.connect('bdd.db')
    curseur= connexion.cursor()
    
    curseur.execute("""
                    DELETE id
                        FROM utilisateur
                        WHERE email=?
                        """, (email,))
    connexion.commit()
    connexion.close()


def suppr_action(entreprise:str) ->None:
    connexion=sqlite3.connect('bdd_newest.db')
    curseur= connexion.cursor()
    
    curseur.execute("""
                    DELETE FROM action
                        WHERE entreprise=?
                        """, (entreprise,))
    connexion.commit()
    connexion.close()
    
