from calculadora import Calculadora

def test_add():
    calc = Calculadora()
    assert calc.add(2, 3) == 5

def test_substract():
    calc = Calculadora()
    assert calc.substract(3, 2) == 1
