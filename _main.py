import menu, login


def main():
    admin = 'admin'
    vendedor = 'vendedor'
    permissao = 'no_permission'
    credenciais =  menu.login()
    
    login_dic : str
    login_usr : str
    senha_dic : str
    senha_usr : str

    for elto in login.credencial_admin: #serve pra varrer o dicionário
        login_dic = elto.replace(' ', '').lower()
        login_usr = credenciais[0].replace(' ', '').lower()
        senha_dic = login.credencial_admin[elto].replace(' ', '').lower()
        senha_usr = credenciais[1].replace(' ', '').lower()
        if login_dic == login_usr:
            if senha_dic == senha_usr:
                permissao = admin
                if menu.menu_usr(permissao) == '1':
                    menu.estoque()

    
    if permissao != admin:
        for elto in login.credencial_proletario:
            login_dic = elto.replace(' ', '').lower()
            login_usr = credenciais[0].replace(' ', '').lower()
            senha_dic = login.credencial_proletario[elto].replace(' ', '').lower()
            senha_usr = credenciais[1].replace(' ', '').lower()

            if login_dic == login_usr:
                if senha_dic == senha_usr:
                    permissao = vendedor
                    menu.menu_usr(permissao)
    if permissao != admin and permissao != vendedor:
        print('\33[1;31mERRO: Login ou senha inválidos, tente novamente\33[m')
    print('\33[1,92mpermissao:\33[m',permissao)
    

    input()
    return 0

main()

