import pytest
from imc import calc_imc
import math

@pytest.mark.parametrize("peso, alt, imc", [
    (98, 1.70, 33.91), #Obsidade II
    (69, 1.62, 26.29), #Obsidade I
    (200, 1.62, 76.21), #Obsidade III
    (59, 1.62, 22.48), #Normal
    (0, 0, None), # Falha
    (45, 1.62, 17.15) #Magreza
])
def test_calc_imc(peso, alt, imc):
    assert calc_imc(peso, alt) == pytest.approx(imc, abs=0.01)