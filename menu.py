import os
import itertools
import math
import time
import login
import re


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
        print('###############################################')
        escolha = input()
        return escolha
    elif permissao == 'vendedor':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('##############CONTROLE DE ESTOQUE##############')
        print('#                                             #')
        print('#  Exibir produto(s), Digite(1)               #')
        print('#                                             #')
        print('#  Voltar para a tela de login, Digite(5)     #')
        print('#                                             #')
        print('#  Seu nível de permissão atual é de \33[92mVENDEDOR\33[m #')
        print('#                                             #')
        print('###############################################')
        escolha = input()
        return escolha


def add_prod():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('##############CONTROLE DE ESTOQUE##############')
        print('#                                             #')
        print('#             Adicionando Produto             #')
        print('#      (deixe em branco se quiser voltar)     #')
        print('#                                             #')
        print('###############################################')
        print('#                                             #')
        print('#  Nome do Produto:',end='')
        nome = str(input())
        print('#  Quantidade:',end='')
        quant = str(input())
        print('#                                             #')
        print('###############################################')
        print('#                                             #')
        print('#        Digite (r) para prosseguir ou        #')
        print('#  digite (s) para voltar ao menu de usuário  #')
        print('#                                             #')
        print('###############################################')
        opcao = str(input())
        if opcao == 'r':
            estoque = open('estoque.txt','r')
            produtos = estoque.readlines()
            print(produtos)
            cont = 0
            for index in produtos:
                if nome in produtos[cont]:
                    print('\33[1;31mERRO: Produto já existe, tente novamente\33[m')
                    time.sleep(1.500)
                    estoque.close()
                cont += 1
            if len(nome) > 20 or len(quant) > 10:
                print('\33[1;31mERRO: Nome ou quantidade inválidos, tente novamente\33[m')
                time.sleep(.500)
            elif not quant.isnumeric():
                print('\33[1;31mERRO: Quantidade Inválida, tente novamente\33[m')
                time.sleep(.500)
            else:
                estoque.close()
                estoque = open("estoque.txt", 'a')
                estoque.write('\n' + nome + ';' + quant)
                print('\33[1;92mProduto adicionado com sucesso\33[m')
                time.sleep(.500)
                estoque.close()
        elif opcao == 's':
            break
            estoque.close()
        else:
            print('\33[1;31mERRO: Comando Inválido, tente novamente\33[m')
            time.sleep(.500)
    
def edit_prod():
    while True:
        #os.system('cls' if os.name == 'nt' else 'clear')
        print('##############CONTROLE DE ESTOQUE##############')
        print('#                                             #')
        print('#         Qual produto deseja editar?         #')
        print('#                                             #')
        print('###############################################')
        print('#                                             #')
        print('#  Nome do Produto: ', end='')
        nome = str(input())
        print('#                                             #')
        print('###############################################')
        print('#                                             #')
        print('#        Digite (r) para prosseguir ou        #')
        print('#  digite (s) para voltar ao menu de usuário  #')
        print('#                                             #')
        print('###############################################')
        opcao = str(input())
        if opcao == 'r':
            estoque = open('estoque.txt','r')
            produtos = estoque.readlines()
            num_lines = sum(1 for line in estoque)
            lista_estoque = []
            print(produtos)
            check = 0
            for index in produtos:
                index = index[:-1]
                linhas = index.split(';')
                lista_estoque.append(linhas)
            for cont in range(len(lista_estoque)):
                if lista_estoque[cont][0] == nome:
                    edit_prod_2(lista_estoque[cont][0],lista_estoque[cont][1])
                    break
                else:
                    check = 1
            if check == 1:
                print('\33[1;31mERRO: Produto não encontrado, tente novamente\33[m')
                time.sleep(.500)

        elif opcao == 's':
            break
        else:
            print('\33[1;31mERRO: Comando Inválido, tente novamente\33[m')
            time.sleep(.500)

def edit_prod_2(nome,quant):
    while True:
        #os.system('cls' if os.name == 'nt' else 'clear')
        print('##############CONTROLE DE ESTOQUE##############')
        print('#                                             #')
        print('#        Editando {:^20}        #'.format(nome))
        print('#                                             #')
        print('###############################################')
        print('#                                             #')
        print('#  Para alterar a quantidade, Digite(1)       #')
        print('#  Para alterar o nome, Digite(2)             #')
        print('#  Para remover o produto, Digite(3)          #')
        print('#  Para voltar ao menu de usuário, Digite(4)  #')
        print('#                                             #')
        print('#                                Qtd.         #')
        print('#     {:<20}     {:^10}     #'.format(nome,quant))
        print('#                                             #')
        print('###############################################')
        opcao = str(input())
        if opcao == '1':
            altera_quant()
        elif opcao == '2':
            altera_nome()
        elif opcao == '3':
            remove_prod()
        
    
def altera_quant():
    while True:
        print('##############CONTROLE DE ESTOQUE##############')
        print('#                                             #')
        print('#            Alterando  Quantidade            #')
        print('#                                             #')
        print('###############################################')
        print('#                                             #')
        print('#  Quantidade: ', end='')
        quant = str(input())
        print('#                                             #')
        print('###############################################')
        print('#                                             #')
        print('#        Digite (r) para prosseguir ou        #')
        print('#  digite (s) para voltar ao menu de usuário  #')
        print('#                                             #')
        print('###############################################')
        opcao = str(input())

def altera_nome():
    return 0
def remove_prod():
    return 0 


def cadastro_usr(adm,vnd):
    while True:
        #os.system('cls' if os.name == 'nt' else 'clear')
        print('##############CONTROLE DE ESTOQUE##############')
        print('#                                             #')
        print('#            Cadastro Novo Usuário            #')
        print('#                                             #')
        print('###############################################')
        print('#                                             #')
        print('#  Login: ',end='')
        login = str(input())
        print('#  Senha: ',end='')
        senha = str(input())
        print('#  Nível de permissão (ADM/VND): ',end='')
        perm = str(input())
        print('#                                             #')
        print('###############################################')
        print('#                                             #')
        print('#        Digite (r) para prosseguir ou        #')
        print('#  digite (s) para voltar ao menu de usuário  #')
        print('#                                             #')
        print('###############################################')
        opcao = str(input())

        regex = re.compile('[@_!#$%^&*()<>?/\|{}~:]')
        if opcao == 'r':
            if login in adm or login in vnd:
                print('\33[1;31mERRO: Usuário já existe, tente novamente\33[m')
                time.sleep(.500)
            elif len(login) < 4 or len(login) > 15:
                print('\33[1;31mERRO: Dados Inválidos, tente novamente\33[m')
                time.sleep(.500)
            elif len(senha) < 4 or len(senha) > 15:
                print('\33[1;31mERRO: Dados Inválidos, tente novamente\33[m')
                time.sleep(.500)
            elif regex.search(login) != None or regex.search(senha) != None:
                print('A')
                print('\33[1;31mERRO: Dados Inválidos, tente novamente\33[m')
                time.sleep(.500)
            elif perm != 'ADM' and perm != 'VND':
                print('B')
                print('\33[1;31mERRO: Dados Inválidos, tente novamente\33[m')
                time.sleep(.500)
            else:
                if perm == 'ADM':
                    adm[login] = senha
                    print('add_adm')
                    return adm,vnd
                elif perm == 'VND':
                    vnd[login] = senha
                    print('add_vnd')
                    return adm,vnd
        elif opcao == 's':
            break
        else:
            print('\33[1;31mERRO: Comando Inválido, tente novamente\33[m')
            time.sleep(.500)

def altera_dados():
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


