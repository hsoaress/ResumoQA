# Cenário: "Dado um usuário logado, Quando adiciona um item ao carrinho, Então o total deve ser atualizado"

usuario_logado = True
carrinho = {"total": 0}

if usuario_logado:
    carrinho["total"] += 30

assert carrinho["total"] == 30, "Total incorreto no carrinho!"

print("Critério de aceitação passou!")

def realizar_pagamento(saldo, valor_compra):
    if saldo >= valor_compra:
        return "Pagamento aprovado"
    else:
        return "Saldo insuficiente"

# Teste baseado em risco (pagamento é crítico)
assert realizar_pagamento(100, 50) == "Pagamento aprovado"
assert realizar_pagamento(50, 100) == "Saldo insuficiente"

print("Testes críticos de pagamento passaram!")
