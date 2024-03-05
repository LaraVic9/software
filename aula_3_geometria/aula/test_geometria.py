import pytest
import geometria as geo
import math
# realiza os test unitarios do arquivo geometria.py


@pytest.mark.parametrize("raio,area",[(1, 3.14159)])

def test_calc_area_circulo_many(raio, area):
    assert geo.calcular_area_circulo(raio) == pytest.approx(area)


class TestAreas:
    def test_calcular_area_quadrado(self):
        assert 16 == geo.calcular_area_quadrado(4)
        assert geo.calcular_area_quadrado(-4) is None
        assert geo.calcular_area_quadrado(0) == 0
        
   # def test_calc_area_circulo():
      #  assert geo.calc_area_circulo(0) == pytest.approx(0)
      #  assert geo.calc_area_circulo(1) == pytest.approx(3.14159)
      #  assert geo.calc_area_circulo(1) == pytest.approx(3.1416) # fail - baixa precisao
      #  assert geo.calc_area_circulo(2) == pytest.approx(12.56637061)
        
    def test_calcular_area_triangulo(self):
        assert geo.calcular_area_triangulo(2,2) == 2
        assert geo.calcular_area_triangulo(-2,-2) is None 
        assert geo.calcular_area_triangulo(0,0) == 0
        
