def calcular_desconto(valor, percentual):
    return valor - (valor * percentual / 100)

# Teste unitário
def test_calcular_desconto():
    assert calcular_desconto(100, 10) == 90
    assert calcular_desconto(200, 25) == 150

test_calcular_desconto()
