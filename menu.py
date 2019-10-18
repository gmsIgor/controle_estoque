def login():
    print('#############################################')
    print('#            CONTROLE DE ESTOQUE            #')
    print('#         digite o login:', end=' ')
    usuario = str(input())
    print('#         digite a senha:', end=' ')
    senha = str(input())
    
    credenciais = [usuario,senha]
    return credenciais