import sqlite3

connexion = sqlite3.connect("bdd.db")   #Se connecter à la base de données

curseur = connexion.cursor() #SQL.sh pour apprender SQL
#####################################################
curseur.execute(""" 
       CREATE TABLE IF NOT EXISTS utilisateur(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          nom TEXT NOT NULL,
          email TEXT NOT NULL,
          est_actif BOOLEAN NOT NULL,
          mdp TEXT NOT NULL,
          cle_jwt TEXT NOT NULL
            )
""")
connexion.commit()
######################################################
curseur.execute(""" 
       CREATE TABLE IF NOT EXISTS action(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            entreprise TEXT NOT NULL,
            prix INTEGER NOT NULL
            )
""")
connexion.commit()
######################################################
curseur.execute(""" 
       CREATE TABLE IF NOT EXISTS asso_suivi_suiveur(
            suiveur_id INTEGER,
            suivi_id INTEGER,
            FOREIGN KEY(suiveur_id) REFERENCES utilisateur(id),  
            FOREIGN KEY(suivi_id) REFERENCES utilisateur(id)          
       
)
""")
connexion.commit()
#####################################################
curseur.execute(""" 
       CREATE TABLE IF NOT EXISTS carnet_operation(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            action_id INTEGER,
            prix_achat INTEGER NOT NULL,
            date_achat TEXT NOT NULL,
            prix_vente INTEGER NULL,
            date_vente TEXT NULL,
            FOREIGN KEY(user_id) REFERENCES utilisateur(id),
            FOREIGN KEY(action_id) REFERENCES action(id)          
)
""")
connexion.commit()