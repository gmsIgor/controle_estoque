import menu
import login

def main():
    ADMIN = 'admin'
    VENDEDOR = 'vendedor'
    permissao = 'no_permission'
    credenciais =  menu.login()

    credencia(login.credencial_admin, credenciais, ADMIN)

    if permissao != ADMIN:
        credencia(login.credencial_proletario, credenciais, VENDEDOR)

    if permissao != ADMIN and permissao != VENDEDOR:
        print('\33[1;31mERRO: Login ou senha inválidos, tente novamente\33[m')
    print('\33[1,92mpermissao:\33[m',permissao)

def credencia(credencial, credenciais, perm):
    login_dic : str
    login_usr : str
    senha_dic : str
    senha_usr : str

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
                    elif permissao == 'admin':
                        if escolha == '2':
                            menu.add_prod()
                        if escolha == '3':
                            menu.edit_prod()
                        if escolha == '4':
                            menu.cadastro_usr(login.credencial_admin,login.credencial_proletario)
                    #elif escolha == '5':  #Não sei voltar para o menu de login
main()