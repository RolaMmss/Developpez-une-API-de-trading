import sqlite3



def creer_utilisateur(nom:str, email:str, mdp:str, cle_jwt:str) -> None: 
    connexion = sqlite3.connect("bdd.db")   #Se connecter à la base de données

    curseur = connexion.cursor() #SQL.sh pour apprender SQL

    curseur.execute(""" 
        INSERT INTO utilisateur 
            VALUES (NULL, ?, ?, ?, ?)           
    """, (nom,email,mdp,cle_jwt))        # VALUES (NULL, 'Rola', 'rola@rola.com', 'azerty123')
    connexion.commit()

    connexion.close()

creer_utilisateur('Rola', 'rola@rola.com', 'azerty123','clerola')
creer_utilisateur('Manu', 'manu@gmail.com', 'azerty1234','clemanu')


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
    
    
    
def creer_carnet_operations(user_id:int, action_id:int, prix_achat:int, date_achat:str, prix_vente:int, date_vente:str) -> None:
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()

    curseur.execute("""
                    INSERT INTO carnet_operations
                        VALUES ( NULL,?, ?, ?, ?, NULL, NULL)   
                    """, (user_id, action_id, prix_achat, date_achat, prix_vente, date_vente))
    connexion.commit()
# qd il y a points d'interrogation >>>il va chercher la valeur qui sera donnée plus tard)cf : .format()
    connexion.close()

def creer_carnet_operations(user_id:int, action_id:int, prix_achat:int, date_achat:str, prix_vente:int, date_vente:str) -> None:
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()

    curseur.execute("""
                    UPDATE carnet_opreations
                        VALUES ( NULL,?, ?, ?, ?, ?, ?)   
                    """, (user_id, action_id, prix_achat, date_achat, prix_vente, date_vente))
    connexion.commit()
# qd il y a points d'interrogation >>>il va chercher la valeur qui sera donnée plus tard)cf : .format()
    connexion.close()

def modifier_playlist(id:int, date_vente:str, prix_vente:str)->None:
    connexion=sqlite3.connect('bdd.db')
    curseur= connexion.cursor()
    
    curseur.execute("""
                    UPDATE carnet_opreations
                        SET  date_vente= ?
                        SET prix_vente=?
                        WHERE id= ?
                 
                        """, (date_vente, prix_vente, id))
    
    connexion.commit()
    connexion.close()
    
    
def creer_action(entreprise:str, prix:int) -> None:
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()

    curseur.execute("""
                    INSERT INTO utilisateur 
                        VALUES (NULL, ?, ?)   
                    """, (entreprise, prix))
    connexion.commit()
# qd il y a points d'interrogation >>>il va chercher la valeur qui sera donnée plus tard)cf : .format()
    connexion.close()