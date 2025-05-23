# Critérios de aceitação com BDD simulado

# Cenário: "Dado um usuário logado, Quando adiciona um item ao carrinho, Então o total deve ser atualizado"

usuario_logado = True
carrinho = {"total": 0}

if usuario_logado:
    carrinho["total"] += 30

assert carrinho["total"] == 30, "Total incorreto no carrinho!"

print("Critério de aceitação passou!")



#Saída:
        #Critério de aceitação passou!

