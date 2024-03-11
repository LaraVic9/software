from npc_player import *

def test_get_npc_tipo():
    esperado = ["dragon", "troll"]
    #esperado = ["troll", "dragon"] # FALHA

    assert get_npc_tipo() == esperado 
    

def test_get_npc_saude():
    esperado = {"dragon": 100, "troll": 70}
    #esperado = {"dragon": 100, "troll": 90} # FALHA

    assert get_npc_saude() == esperado
    
# pytest -v src/npc 
# resultado do teste ( 50%, 100%)