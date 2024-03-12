import math
#Exercicio 1 

#Criar 3 casos de teste para a funcao que faz o calculo do IMC
# Peso 70, altura 1.70 - IMC == 24.2

#slides justpaste.it/da00f

def calc_imc(peso, alt):
    if alt == 0:
        return None
    return round(peso / (alt ** 2), 2)


