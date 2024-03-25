import math
# calcular a area

def calcular_area_quadrado(lado):
    if lado < 0: 
        return None
    return lado * lado

def calcular_area_circulo(raio):
    if raio < 0:
        return None
    return math.pi * (raio * raio)

def calcular_area_triangulo(alt, base):
    if base < 0 or alt < 0:
        return None
    return (base * alt)//2

# implementar: circulo, triangulo, retangulo

def calc_losangulo(r):
    print('calc')