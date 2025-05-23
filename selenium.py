# No Colab, Selenium não funciona bem sem configuração de ambiente.
# Simulando automação de login com função.

def testar_login(usuario, senha):
    if usuario == "admin" and senha == "1234":
        return "Login bem-sucedido"
    else:
        return "Falha no login"

# Teste
assert testar_login("admin", "1234") == "Login bem-sucedido"
assert testar_login("user", "1234") == "Falha no login"

print("Testes de login passaram!")

#Saída: 
    #Testes de login passaram!
