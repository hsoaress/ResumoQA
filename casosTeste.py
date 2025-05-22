# Casos de teste: priorizando módulo de pagamento

def realizar_pagamento(saldo, valor_compra):
    if saldo >= valor_compra:
        return "Pagamento aprovado"
    else:
        return "Saldo insuficiente"

# Teste baseado em risco (pagamento é crítico)
assert realizar_pagamento(100, 50) == "Pagamento aprovado"
assert realizar_pagamento(50, 100) == "Saldo insuficiente"

print("Testes críticos de pagamento passaram!")
