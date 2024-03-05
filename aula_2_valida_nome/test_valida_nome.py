# validar se nome do usuario possui mais de 4 caracteres

from valida_nome import valida_nome

def test_valida():
   assert valida_nome(4,"lara") == 4