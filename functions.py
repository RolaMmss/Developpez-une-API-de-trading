

from crud import creer_utilisateur, creer_asso_suivi_suiveur, creer_carnet_operations, inserer_vente_operations, modifier_carnet_operations, creer_action, recup_jeton_w_mail_mdp, recup_id_w_jeton,recup_id_avec_mail, delete_user




# creer_utilisateur('manu', 'ola@ola.fr', 'mano', 'ola1')

# creer_asso_suivi_suiveur(1,2)

# creer_carnet_operations(1,2,38,'28/3')



inserer_vente_operations(1, '23', 12)
creer_action('tres', 2)

# modifier_carnet_operations(1, 'tres', 'trop',)
print(recup_id_avec_mail("rola@rola.com"))

print(recup_jeton_w_mail_mdp("rola@rola.com", "azerty123"))

print(recup_id_w_jeton("clemanu"))

print(delete_user("ola@ola.fr"))