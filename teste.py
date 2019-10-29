def add_prod():
    escolha = 1
    estoquelist=[]
    estoque = open("estoque.txt",'a')
    
    while escolha == 1:
        nome = input('entre com o nome do item  ')
        quantidade = int(input('Entre com a quantidade do item  '))
        produto = {"Nome:": nome,"quantidade:": quantidade} 
        escolha = int(input ('digite(1) para continuar editando ou (2) para sair  '))
        if escolha < 1 or escolha > 2:
            print('Entre com uma opcao valida')
            escolha = int(input('digite(1) para continuar editando ou (2)'))
        estoquelist.append(produto) 
        contador = 0
        for contador in range (0,len(estoquelist)):

            estoque.write(str(estoquelist[contador]['Nome:']) + ';' + str(estoquelist[contador]['quantidade:']) + '\n')


      
    

add_prod()




def exibir_estoque():
    contador = 0
    estoque = open('estoque.txt','r')
    for i in estoque:
        print(i ,';','\n')
    estoque.close()
exibir_estoque()    








