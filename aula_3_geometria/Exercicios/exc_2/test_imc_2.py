from imc_2 import calcula_imc
import pytest 

@pytest.mark.parametrize("peso, alt, imc", [
    (50, 1.80, 'Magreza'), #ACERTO
    #(70, 1.80, 'Magreza'), # FALHA
    (70, 1.75, 'Normal'), # ACERTO
    #(80, 1.75, 'Normal'), # FALHA
    (80, 1.75, 'Sobrepeso'), # ACERTO
    #(100, 1.75, 'Sobrepeso'), # FALHA
    (100, 1.75, 'Obesidade grau I'), #ACERTO
    #(114, 1.75, 'Obesidade grau I'), # FALHA
    (114, 1.75, 'Obesidade grau II'), # ACERTO
    #(127, 1.75, 'Obesidade grau II'), # FALHA
    (130, 1.75, 'Obesidade grau III'), # ACERTO
    #(127, 1.75, 'Obesidade grau III') # FALHA
    #(0, 0, 1)
])

def test_calc_imc(peso, alt, imc):
    assert calcula_imc(peso, alt) == pytest.approx(imc, abs=0.01)