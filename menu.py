import os

def login():
    print('#############################################')
    print('#            CONTROLE DE ESTOQUE            #')
    print('#############################################')
    print('#                                           #')
    print('#   Digite o login:', end=' ')
    usuario = str(input())
    print('#   Digite a senha:', end=' ')
    senha = str(input())
    print('#                                           #')
    print('#############################################')
    
    credenciais = [usuario,senha]
    return credenciais

def menu_usr(permissao):
    if permissao == 'admin':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('##############CONTROLE DE ESTOQUE##############')
        print('#                                             #')
        print('#  Exibir produto(s), Digite(1)               #')
        print('#                                             #')
        print('#  Adicionar produto(s), Digite(2)            #')
        print('#                                             #')
        print('#  Editar produto(s), Digite(3)               #')
        print('#                                             #')
        print('#  Cadastrar novo funcionário, Digite(4)      #')
        print('#                                             #')
        print('#  Voltar para a tela de login, Digite(5)     #')
        print('#                                             #')
        print('#  Seu nível de permissão atual é de \33[36mADM\33[m      #')
        print('#                                             #')
        print('###########3###################################')
        escolha = input()
        return escolha
    elif permissao == 'vendedor':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('##############CONTROLE DE ESTOQUE##############')
        print('#                                             #')
        print('#  Exibir produto(s), Digite(1)               #')
        print('#                                             #')
        print('#  Seu nível de permissão atual é de \33[92mVENDEDOR\33[m #')
        print('#                                             #')
        print('###############################################')
        escolha = input()
        return escolha

def estoque():
    pg = 1
    estoque = open('estoque.txt')
    while True:
        print(pg, 'aquiiiiiiiiiiiiiiiiiiiiiiiiiiii')
        print('##############CONTROLE DE ESTOQUE##############')
        print('#                                             #')
        print('#      Produtos                Quantidade     #')
        print('#                                             #')
        for i, line in enumerate(estoque):
            linha = line.replace('\n', '')
            info = linha.split(';') 
            print(info[1], '         ', info[2])
            if i == 3:
                print('pág.', pg)
                print('(a) voltar pág. | proxima pág. (d)')
                break
        opcao = str(input())
        if opcao == 'a' and pg != 1:
            pg -= 1
        elif opcao == 'd':
            pg += 1