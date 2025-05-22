# Cenário: Dado um usuário no carrinho, Quando adiciona um produto de R$50, Então o total deve ser R$50

# Dado
carrinho = {"total": 0}

# Quando
carrinho["total"] += 50

# Então
assert carrinho["total"] == 50, f"Falha: total = {carrinho['total']}, esperado 50"

print("Teste de aceitação passou!")
