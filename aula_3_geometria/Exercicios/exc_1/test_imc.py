import pytest
from imc import calcular_imc
import math

def test_calcular_imc():
    assert 24.22 == round(calcular_imc(70,1.70), 2)
    assert calcular_imc(0,0) is None
    assert calcular_imc(-2,-2) is None