def login():
    print('#############################################')
    print('#            CONTROLE DE ESTOQUE            #')
    print('#         digite o login:', end=' ')
    usuario = str(input())
    print('#         digite a senha:', end=' ')
    senha = str(input())
    
    credenciais = [usuario,senha]
    return credenciais

def lobby(permissao):
    print('#############################################')
    print('#            CONTROLE DE ESTOQUE            #')
    print('#############################################')
    print('#    Digite:                                #')
    print('#    1)Para exibir produto(s)               #')
    print('#    2)Para editar protuo(s)                #')
    print('#seu nivel de permissao é', permissao.upper)