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
#######################################################################################""

