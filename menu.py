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
            produtos = estoque.read()
            if nome in produtos:
                print('\33[1;31mERRO: Produto já existe, tente novamente\33[m')
                estoque.close()
            elif len(nome) > 20 or len(quant) > 10:
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
    
def edit_prod(permissao):
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
        print('#  Nível de permissão: ',end='')
        perm = str(input())
        print('#  (ADM/VND)                                  #')
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


