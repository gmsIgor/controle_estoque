def criar_estoque():
    escolha = 1
    estoquedic=[]
    estoque = open("estoque.txt",'a')
    while escolha == 1:
        nome = input('entre com o nome do item  ')
        quantidade = int(input('Entre com a quantidade do item  '))
        produto = {"Nome:": nome,"quantidade:": quantidade}
        escolha = int(input ('digite(1) para continuar editando ou (2) para sair  '))
        estoquedic.append(produto) 
        estoque.writelines(str(produto.items())+ '\n')
    
    for i in produto:
        print(str(produto.values()))
    return(estoquedic)
  


def editar_estoque(estoquedic):
    escolha = 1
    estoquedic=[]
    estoque = open('estoque.txt','r+')
    while escolha == 1:
        nome = input('Entre com o nome do produto  ')
        quantidade = int(input ('Entre com a quantidade de',nome,':'))
        produto = {"Nome:": nome,"quantidade:":quantidade}
        escolha = int(input('Digite(1) para continuar editando e (2) para sair'))
        estoquedic.append(produto)
        estoque.writelines(str(produto.items())+'\n')
    for i in produto: 
        print(str(produto.values()))
    return(estoquedic)


editar_estoque(estoquedic)
