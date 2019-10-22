to].replace(' ', '').lower()
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