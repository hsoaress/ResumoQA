def logar_mensagem(msg, dados_sensiveis=False):
    if dados_sensiveis:
        raise ValueError("Erro: Não permitido logar dados sensíveis.")
    print(f"LOG: {msg}")

# Teste seguro
logar_mensagem("Usuário fez login")

# Teste com dado sensível
try:
    logar_mensagem("Senha: 123456", dados_sensiveis=True)
except ValueError as e:
    print(e)
