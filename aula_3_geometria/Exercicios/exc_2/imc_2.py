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

def calcula_imc(peso, alt):
    
    imc = peso / (alt ** 2)
    
    if alt < 0 or peso < 0:
        return None
    
    if imc < 18.50:
       return 'Magreza'
    elif 18.50 <= imc < 24.99:
       return 'Normal'
    elif 25.00 <= imc < 30.00:
       return 'Sobrepeso'
    elif 30.00 <= imc < 35.00:
        return 'Obesidade grau I'
    elif 35.00 <= imc < 40.00:
       return 'Obesidade grau II'
    else:
        return 'Obesidade grau III'
    

# nova funcao "classifica_imc" apenas com os IF, em vez de print "magreza" retornar como string
# criar novo test pra classificacao "magreza" etc