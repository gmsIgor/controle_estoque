import menu, login


def main():
    admin = False
    credenciais =  menu.login()

    for elto in login.credencial_admin:
        print(credenciais)
        print(credenciais[0], elto)
        print(credenciais[1], login.credencial_admin[elto])
        if credenciais[0].lower == str(elto.lower):
            print('eita -------------------------')
        if credenciais[0].lower == str(elto.lower) and credenciais[1].lower == str(login.credencial_admin[elto].lower):
            print('deu bom')
            admin = True

    
    return 0

main()

