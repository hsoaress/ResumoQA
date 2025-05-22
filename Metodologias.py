# Simulação: executar testes automaticamente (representação simples)
def rodar_todos_os_testes():
    test_1 = calcular_desconto(100, 10) == 90
    test_2 = verificar_nome_usuario("") == "Erro: Nome é obrigatório."
    return test_1 and test_2

if rodar_todos_os_testes():
    print("Todos os testes passaram. Pronto para deploy!")
else:
    print("Alguns testes falharam.")
