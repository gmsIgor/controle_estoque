import json
import credenciais

"""
credencial_proletario = {}
credencial_admin = {}
"""

def carrega_credenciais():
    data = None
    with open('login.json', 'r') as credFile:
        data = json.load(credFile)

    credenciais.credencial_proletario = data[0]
    credenciais.credencial_admin = data[1]


    return

def salva_credenciais():
    data = [credenciais.credencial_proletario, credenciais.credencial_admin]
    with open('login.json', 'w') as credFile:
        json.dump(data, credFile)

    return

#----- 

def add_cred_prolet(login : str, senha : str):
    credenciais.credencial_proletario[login] = senha

def set_cred_prolet(new_dict):
    credenciais.credencial_proletario = new_dict

def get_cred_prolet():
    return credenciais.credencial_proletario

def remove_cred_prolet(login):
    credenciais.credencial_proletario.pop(login)

def altera_senha_prolet(login, senha):
    credenciais.credencial_proletario[login] = senha


def add_cred_adm(login : str, senha : str):
    credenciais.credencial_admin[login] = senha

def set_cred_adm(new_dict):
    credenciais.credencial_admin = new_dict

def get_cred_adm():
    return credenciais.credencial_admin

def remove_cred_adm(login):
    credenciais.credencial_admin.pop(login)

def altera_senha_adm(login, senha):
    credenciais.credencial_admin[login] = senha