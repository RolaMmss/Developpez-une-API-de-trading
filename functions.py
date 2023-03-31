

from crud import *

# creer_utilisateur('manu', 'ola@ola.fr', 'mano', 'ola1')

# creer_asso_suivi_suiveur(3,4)

# creer_carnet_operations(1,2,38,'28/3')



# inserer_vente_operations(1, '23', 12)
# creer_action('tres', 2)

# # modifier_carnet_operations(1, 'tres', 'trop',)
# print(recup_id_avec_mail("rola@rola.com"))

# print(recup_jeton_w_mail_mdp("rola@rola.com", "azerty123"))

# print(recup_id_w_jeton("clemanu"))

# print(delete_user("ola@ola.fr"))

# creer_action('  Toyota',23000)
# print(actions_personnes_suivies(2))

# print(suppr_personnes_suivie(1,"ola@ola.fr"))
resultats = suppr_personnes_suivie(1,"ola@ola.fr")
if not resultats:
    print("Aucun enregistrement n'a été supprimé.")
else:
    print(f"{len(resultats)} enregistrement(s) ont été supprimé(s).")
print(suppr_action("Toyota"))