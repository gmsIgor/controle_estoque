import os
import itertools
import math
import time
import re
import login as biri
import json
tempo = 1

def login():
    os.system('cls' if os.name == 'nt' else 'clear')
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
        print('#  Alterar dados cadastrais, Digite(5)        #')
        print('#                                             #')
        print('#  Voltar para a tela de login, Digite(6)     #')
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
        print('#  Alterar dados cadastrais, Digite(5)        #')
        print('#                                             #')
        print('#  Voltar para a tela de login, Digite(6)     #')
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
            cont = 0
            for index in produtos:
                if nome in produtos[cont]:
                    print('\33[1;31mERRO: Produto já existe, tente novamente\33[m')
                    time.sleep(tempo)
                    estoque.close()
                cont += 1
            if len(nome) > 20 or len(quant) > 10:
                print('\33[1;31mERRO: Nome ou quantidade inválidos, tente novamente\33[m')
                time.sleep(tempo)
            elif not quant.isnumeric():
                print('\33[1;31mERRO: Nome ou quantidade inválidos, tente novamente\33[m')
                time.sleep(tempo)
            else:
                estoque.close()
                estoque = open("estoque.txt", 'a')
                estoque.write('\n' + nome + ';' + quant)
                print('\33[1;92mProduto adicionado com sucesso\33[m')
                time.sleep(tempo)
                estoque.close()
        elif opcao == 's':
            break
        else:
            print('\33[1;31mERRO: Comando Inválido, tente novamente\33[m')
            time.sleep(tempo)

def procura_prod(produto):
    estoque = open ('estoque.txt','r+')
    estoque.seek(0,0)
    produtos_list = []
    estoque_string = estoque.readlines()
    for line in estoque_string :
        line = line[:-1]
        linha = line.split(';')
        produtos_list.append(linha)
    contador = 0
    produto_em_estoque = 0
    for contador in range (0,len(produtos_list)):
        if produtos_list[contador][0] == produto :
            produto_em_estoque = 1
            return 1
            break
    if produto_em_estoque == 0 :
        return 0



def edit_prod():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('##############CONTROLE DE ESTOQUE##############')
        print('#                                             #')
        print('#         Qual produto deseja editar?         #')
        print('#      (deixe em branco se quiser voltar)     #')
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
            check = 0
            for index in produtos:
                index = index[:-1]
                linhas = index.split(';')
                lista_estoque.append(linhas)
            for cont in range(len(lista_estoque)):
                if lista_estoque[cont][0] == nome:
                    edit_prod_2(lista_estoque[cont][0],lista_estoque[cont][1],lista_estoque,cont)
                    break
                else:
                    check = 1
            if check == 1:
                print('\33[1;31mERRO: Produto não encontrado, tente novamente\33[m')
                time.sleep(tempo)

        elif opcao == 's':
            break
        else:
            print('\33[1;31mERRO: Comando Inválido, tente novamente\33[m')
            time.sleep(tempo)

def edit_prod_2(nome,quant,estoque_lista,cont):
    while True:
        estoque = open('estoque.txt','r')
        for i,line in enumerate(estoque):
            if i == cont:
                line = line[:-1]
                linhas = line.split(';')
        nome = linhas[0]
        quant = linhas[1]
        os.system('cls' if os.name == 'nt' else 'clear')
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
            altera_quant(nome,estoque_lista,cont)
        elif opcao == '2':
            altera_nome(nome,estoque_lista,cont)
        elif opcao == '3':
            remove_prod(nome,estoque_lista,cont,quant)
            break
        
    
def altera_quant(nome,estoque_lista,cont):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('##############CONTROLE DE ESTOQUE##############')
        print('#                                             #')
        print('#            Alterando  Quantidade            #')
        print('#      (deixe em branco se quiser voltar)     #')
        print('#                                             #')
        print('###############################################')
        print('#                                             #')
        print('#  Quantidade: ', end='')
        quant = str(input())
        print('#                                             #')
        print('###############################################')
        print('#                                             #')
        print('#        Digite (r) para prosseguir ou        #')
        print('#   digite (s) para voltar ao menu de edição  #')
        print('#                                             #')
        print('###############################################')
        opcao = str(input())
        if opcao == 'r':
            if not quant.isnumeric():
                print('\33[1;31mERRO: Quantidade inválida, tente novamente\33[m')
                time.sleep(tempo)
            elif len(quant) > 10:
                print('\33[1;31mERRO: Quantidade inválida, tente novamente\33[m')
                time.sleep(tempo)
            else:
                estoque_lista[cont][1] = quant
                estoque = open ('estoque.txt','w')
                contador = 0
                for contador in range (0,len(estoque_lista)):
                    estoque.writelines(str(estoque_lista[contador][0]) + ';'+ str(estoque_lista[contador][1])+'\n')
                estoque.close()
                print('\33[1;92mQuantidade atualizada com sucesso\33[m')
                time.sleep(tempo)
                break
        elif opcao == 's':
            break
        else:
            print('\33[1;31mERRO: Comando Inválido, tente novamente\33[m')
            time.sleep(tempo)
                
def altera_nome(nome,estoque_lista,cont):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('##############CONTROLE DE ESTOQUE##############')
        print('#                                             #')
        print('#               Alterando  Nome               #')
        print('#      (deixe em branco se quiser voltar)     #')
        print('#                                             #')
        print('###############################################')
        print('#                                             #')
        print('#  Novo Nome: ', end='')
        nome = str(input())
        print('#                                             #')
        print('###############################################')
        print('#                                             #')
        print('#        Digite (r) para prosseguir ou        #')
        print('#   digite (s) para voltar ao menu de edição  #')
        print('#                                             #')
        print('###############################################')
        opcao = str(input())
        if opcao == 'r':
            if nome.isnumeric():
                print('\33[1;31mERRO: Nome inválido, tente novamente\33[m')
                time.sleep(tempo)
            elif len(nome) >20:
                print('\33[1;31mERRO: Nome inválido, tente novamente\33[m')
                time.sleep(tempo)
            elif procura_prod(nome) == 1:
                print('\33[1;31mERRO: Nome já usado, tente novamente\33[m')
                time.sleep(tempo)
            else:
                estoque_lista[cont][0] = nome
                estoque = open ('estoque.txt','w')
                contador = 0
                for contador in range (0,len(estoque_lista)):
                    estoque.writelines(str(estoque_lista[contador][0]) + ';'+ str(estoque_lista[contador][1])+'\n')
                estoque.close()
                print('\33[1;92mNome atualizado com sucesso\33[m')
                time.sleep(tempo)
                break
        elif opcao == 's':
            break
        else:
            print('\33[1;31mERRO: Comando Inválido, tente novamente\33[m')
            time.sleep(tempo)
            
def remove_prod(nome,estoque_lista,cont,quant):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('##############CONTROLE DE ESTOQUE##############')
        print('#                                             #')
        print('#              Removendo Produto              #')
        print('#                                             #')
        print('###############################################')
        print('#                                             #')
        print('#        Digite (r) para prosseguir ou        #')
        print('#  digite (s) para voltar ao menu de usuário  #')
        print('#                                             #')
        print('###############################################')
        opcao = str(input())
        if opcao == 'r':
            print('#                                             #')
            print('#  Digite a senha de \33[36mADM\33[m para confirmar: ', end='')
            senha = str(input())
            print('#                                             #')
            print('###############################################')
            for elto in biri.get_cred_adm():
                if senha == biri.get_cred_adm()[elto]:
                    produto = nome
                    procura_prod(produto)
                    for contador in range (0,len(estoque_lista)) :
                        if  estoque_lista[contador][0] == produto :
                            estoque_lista.pop(contador)
                            print(estoque_lista)
                            break
                    estoque = open ('estoque.txt','w')
                    contador = 0
                    for contador in range (0,len(estoque_lista)) :
                        estoque.writelines(str(estoque_lista[contador][0]) + ';'+ str(estoque_lista[contador][1]))
                        if contador <= len(estoque_lista)-2:
                            estoque.write('\n')
                        contador += 1
                    estoque.close()
                    print('\33[1;92mProduto removido com sucesso\33[m')
                    time.sleep(tempo)
                    break
            print('\33[1;31mERRO: Senha incorreta, voltando ao menu de edição\33[m')
            time.sleep(tempo)
            break
        elif opcao == 's':
            break
        else:
            print('\33[1;31mERRO: Comando Inválido, tente novamente\33[m')
            time.sleep(tempo)


def cadastro_usr(adm,vnd):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('##############CONTROLE DE ESTOQUE##############')
        print('#                                             #')
        print('#            Cadastro Novo Usuário            #')
        print('#      (deixe em branco se quiser voltar)     #')
        print('#                                             #')
        print('###############################################')
        print('#                                             #')
        print('#  Login: ',end='')
        login_b = str(input())
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
            if login_b in adm or login_b in vnd:
                print('\33[1;31mERRO: Usuário já existe, tente novamente\33[m')
                time.sleep(tempo)
            elif len(login_b) < 4 or len(login_b) > 15:
                print('\33[1;31mERRO: Dados Inválidos, tente novamente\33[m')
                time.sleep(tempo)
            elif len(senha) < 4 or len(senha) > 15:
                print('\33[1;31mERRO: Dados Inválidos, tente novamente\33[m')
                time.sleep(tempo)
            elif regex.search(login_b) != None or regex.search(senha) != None:
                print('A')
                print('\33[1;31mERRO: Dados Inválidos, tente novamente\33[m')
                time.sleep(tempo)
            elif perm != 'ADM' and perm != 'VND':
                print('B')
                print('\33[1;31mERRO: Dados Inválidos, tente novamente\33[m')
                time.sleep(tempo)
            else:
                if perm == 'ADM':
                    logins = open('login.json','a')
                    biri.add_cred_adm(login_b,senha)
                    biri.salva_credenciais()
                    print('\33[1;92mUsuário cadastrado com sucesso\33[m')
                    time.sleep(tempo)
                    
                elif perm == 'VND':
                    logins = open('login.json','a')
                    biri.add_cred_prolet(login_b,senha)
                    biri.salva_credenciais()
                    print('\33[1;92mUsuário cadastrado com sucesso\33[m')
                    time.sleep(tempo)
        elif opcao == 's':
            break
        else: 
            print('\33[1;31mERRO: Comando Inválido, tente novamente\33[m')
            time.sleep(tempo)

def altera_dados(login_usr,permissao):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('##############CONTROLE DE ESTOQUE##############')
        print('#                                             #')
        print('#          Alterando dados cadastrais         #')
        print('#                                             #')
        print('###############################################')
        print('#                                             #')
        print('#  Para alterar o login, Digite(1)            #')
        print('#  Para alterar a senha, Digite(2)            #')
        print('#  Para voltar ao menu de usuário, Digite(3)  #')
        print('#                                             #')
        print('###############################################')
        opcao = str(input())

        if opcao == '1':
            login_usr = altera_login(login_usr,permissao)
        elif opcao == '2':
            altera_senha(login_usr,permissao)
        elif opcao == '3':
            break

def altera_login(login_usr,permissao):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('##############CONTROLE DE ESTOQUE##############')
        print('#                                             #')
        print('#               Alterando Login               #')
        print('#      (deixe em branco se quiser voltar)     #')
        print('#                                             #')
        print('###############################################')
        print('#                                             #')
        print('# Novo Login: ', end='')
        login = str(input())
        print('#                                             #')
        print('###############################################')
        print('#                                             #')
        print('#        Digite (r) para prosseguir ou        #')
        print('#   digite (s) para voltar ao menu de edição  #')
        print('#                                             #')
        print('###############################################')
        opcao = str(input())
        regex = re.compile('[@_!#$%^&*()<>?/\|{}~:]')
        if opcao == 'r':
            if login in biri.get_cred_adm() or login in biri.get_cred_prolet() :
                print('\33[1;31mERRO: Login já existente, tente novamente\33[m')
                time.sleep(tempo)
            elif len(login) < 4 or len(login) > 15:
                print('\33[1;31mERRO: Login inválido, tente novamente\33[m')
                time.sleep(tempo)
            elif regex.search(login) != None:
                print('\33[1;31mERRO: Login inválido, tente novamente\33[m')
                time.sleep(tempo)
            else:
                if permissao == 'admin':
                    senha = biri.get_cred_adm()[login_usr]
                    biri.remove_cred_adm(login_usr)
                    biri.add_cred_adm(login, senha)
                elif permissao == 'vendedor':
                    senha = biri.get_cred_prolet()[login_usr]
                    biri.remove_cred_prolet(login_usr)
                    biri.add_cred_prolet(login, senha)
                biri.salva_credenciais()
                print('\33[1;92mLogin alterado com sucesso\33[m')
                time.sleep(tempo)
                return login
        elif opcao == 's':
            return login_usr
        else:
            print('\33[1;31mERRO: Comando Inválido, tente novamente\33[m')
            time.sleep(tempo)
    
    
                





def altera_senha(login_usr,permissao):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('##############CONTROLE DE ESTOQUE##############')
        print('#                                             #')
        print('#               Alterando Senha               #')
        print('#      (deixe em branco se quiser voltar)     #')
        print('#                                             #')
        print('###############################################')
        print('#                                             #')
        print('# Nova Senha: ', end='')
        senha = str(input())
        print('#                                             #')
        print('###############################################')
        print('#                                             #')
        print('#        Digite (r) para prosseguir ou        #')
        print('#   digite (s) para voltar ao menu de edição  #')
        print('#                                             #')
        print('###############################################')
        opcao = str(input())
        regex = re.compile('[@_!#$%^&*()<>?/\|{}~:]')
        if opcao == 'r':
            if len(senha) < 4 or len(senha) > 15:
                print('\33[1;31mERRO: Senha inválida, tente novamente\33[m')
                time.sleep(tempo)
            elif regex.search(senha) != None:
                print('\33[1;31mERRO: Senha inválida, tente novamente\33[m')
                time.sleep(tempo)
            else:
                if permissao == 'admin':
                    biri.altera_senha_adm(login_usr,senha)
                elif permissao == 'vendedor':
                    biri.altera_senha_prolet(login_usr,senha)
                biri.salva_credenciais()
                print('\33[1;92mSenha alterada com sucesso\33[m')
                time.sleep(tempo)
                break
        elif opcao == 's':
            break
        else:
            print('\33[1;31mERRO: Comando Inválido, tente novamente\33[m')
            time.sleep(tempo)
        


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
        elif escolha == 's':
            break


