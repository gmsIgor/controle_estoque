import menu
import login
import time


def main():
    
    permissao = 'no_permission'

    while True:
        login.carrega_credenciais()
        
        ADMIN = 'admin'
        VENDEDOR = 'vendedor'
        
        credenciais =  menu.login()

        permissao = credencia(login.get_cred_adm(), credenciais, ADMIN)

        if permissao != ADMIN:
            permissao = credencia(login.get_cred_prolet(), credenciais, VENDEDOR)

        if permissao == 'no_permission':
            print('\33[1;31mERRO: Login ou senha inválidos, tente novamente\33[m')
            time.sleep(2)

def credencia(credencial, credenciais, perm):
    login_dic : str
    login_usr : str
    senha_dic : str
    senha_usr : str
    permissao = 'no_permission'    

    for elto in credencial: #serve pra varrer o dicionário
        login_dic = elto.replace(' ', '').lower()
        login_usr = credenciais[0].replace(' ', '').lower()
        senha_dic = credencial[elto].replace(' ', '').lower()
        senha_usr = credenciais[1].replace(' ', '').lower()
        if login_dic == login_usr:
            if senha_dic == senha_usr:
                permissao = perm
                while True:
                    escolha = menu.menu_usr(permissao)
                    if escolha == '1':
                        menu.estoque(permissao)
                    elif escolha == '5':
                        menu.altera_dados(login_usr,permissao)
                    elif escolha == '6':
                        break
                    elif permissao == 'admin':
                        if escolha == '2':
                            menu.add_prod()
                        if escolha == '3':
                            menu.edit_prod()
                        if escolha == '4':
                            menu.cadastro_usr(login.get_cred_adm(),login.get_cred_prolet())
                    
    return permissao
main()