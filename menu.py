import os
import itertools
import math

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

def add_prod():
    escolha = 1
    estoquelist=[]
    estoque = open("estoque.txt",'r+')
    num_lines = sum(1 for line in estoque)
    while escolha == 1:
        nome = input('entre com o nome do item  ')
        quantidade = int(input('Entre com a quantidade do item  '))
        produto = {"Nome:": nome,"quantidade:": quantidade} 
        escolha = int(input ('digite(1) para continuar editando ou (2) para sair  '))
        while escolha != 1 and escolha!= 2:
            
            print('Entre com uma opcao valida')
            escolha = int(input('digite(1) para continuar editando ou (2)'))
            
        estoquelist.append(produto) 
        contador = 0
       
        for contador in range (0,len(estoquelist)):

            estoque.write(str(estoquelist[contador]['Nome:']) + ';' + str(estoquelist[contador]['quantidade:']) + '\n')
        



    
def edit_prod(permissao):
    return 0

def estoque(permissao):
    pg = 1
    linha = 5
    linhaant = 0
    linhatemp = 0
    estoque = open('estoque.txt','r')
    num_lines = sum(1 for line in estoque)
    pgtot = math.ceil(num_lines/5)
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('##############CONTROLE DE ESTOQUE##############')
        print('#                                             #')
        print('#      Produtos                Quantidade     #')
        print('#                                             #')
        with open('estoque.txt','r') as estoque:
            for line in itertools.islice(estoque,linhaant,linha):
                words = line.replace('\n','')
                info = words.split(';')
                print('#   %-20s        %10s    #'%(info[0],info[1]))
        print('#                                             #')
        print('#                   pág {}/%-3s                 #'.format(pg)%(pgtot))
        print('#       (a) voltar pág | próxima pág (d)      #')
        print('#                                             #')
        print('#        voltar para o menu de usuário        #')
        print('#                  digite(s)                  #')
        print('#                                             #')
        print('###############################################')
        escolha = input()
        if escolha == 'a':
            linha = linhaant
            linhaant -= 5
            pg -= 1
            if linhaant <= 0:
                linha = 5
                linhaant = 0
                pg = 1
        elif escolha == 'd':
            linhatemp = linhaant
            linhaant = linha
            linha += 5
            pg += 1
            if linha >= num_lines:
                if linhaant >= num_lines:
                    linhaant = linhatemp
                linha = num_lines
                pg = pgtot
            print(linhatemp)
            print(linhaant)
            print(linha)
        elif escolha == 's':
            break


