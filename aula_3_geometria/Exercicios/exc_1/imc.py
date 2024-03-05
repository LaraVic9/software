import math
#Exercicio 1 

#Criar 3 casos de teste para a funcao que faz o calculo do IMC
# Peso 70, altura 1.70 - IMC == 24.2

#slides justpaste.it/da00f

def calcular_imc(peso, alt):
    if peso <= 0 or alt <= 0:
        return None
    return peso / (alt * alt)
    


