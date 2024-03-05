# Exercicio 2

# Criar casos de teste para testar a função que faz a classificação do IMC 
# calculado considerando as classes conforme a imagem abaixo. 
# Exemplo: se IMC é 18, a função retorna "Magreza":

# menos que 18.5 == magreza
# 18.5 a 24.9 == normal
# 25 a 29.9 == sobrepeso
# 30 a 34.9 == Obesidade grau I
# 35 a 39.9 == obesidade grau II
# maior que 40 == Obesidade grau III

#slides justpaste.it/da00f

def calculo_imc(peso, alt):
    
    if alt < 0 or peso < 0:
        return None
    
    if (peso / (alt*alt)) >= 18.50:
       return print("Magreza")
    #if (peso / (alt*alt)) >= 18.50 or (peso * (alt*alt)) >= 24.99:
    #   return print("Normal")
    #if (peso / (alt*alt)) >= 25.00 or (peso * (alt*alt)) >= 29.99:
    #   return print("sobrepeso")
    #if (peso / (alt*alt)) >= 30.00 or (peso * (alt*alt)) >= 34.99:
    #    return print("Obesidade grau I")
    # if (peso / (alt*alt)) >= 35.00 or (peso * (alt*alt)) >= 39.99:
    #   return print("Obesidade grau II")
    #if (peso / (alt*alt)) >= 40.00:
    #    return print("Obesidade grau III")
    return peso / (alt * alt)

# nova funcao "classifica_imc" apenas com os IF, em vez de print "magreza" retornar como string
# criar novo test pra classificacao "magreza" etc