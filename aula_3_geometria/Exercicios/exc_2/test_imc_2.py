import pytest
from imc_2 import calculo_imc
import math

def test_calculo_imc_2():
    assert 24.22 == round(calculo_imc(70,1.70), 2)
    #assert calculo_imc(0,0) is None
    assert calculo_imc(-2,-2) is None
    
