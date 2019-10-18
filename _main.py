import menu, login


def main():
    admin = False
    credenciais =  menu.login()

    for elto in login.credencial_admin:
        print(credenciais)
        #print(elto)
        #print(login.credencial_admin[elto])
        if credenciais[0].lower == str(elto.lower) and credenciais[1].lower == str(login.credencial_admin[elto].lower):
            print('deu bom')
            admin = True

    
    return 0

main()

