def add_prod():
    escolha = str(1)
    estoquelist=[]
    estoque = open("estoque.txt",'r+')
    num_lines = sum(1 for line in estoque)
    while escolha == str(1):
        nome = input('entre com o nome do item  ')
        quantidade = input('Entre com a quantidade do item  ')
        while not quantidade.isnumeric()  :
            print('Entre com uma opção válida  : \n')
            escolha = input('digite (1) para continuar ou (2) para sair \n')
            quantidade = input('Entre com a nova quantidade')
        while int(quantidade) < 0 :
            print('Entre com uma opção válida : \n')
            
            escolha = input('digite (1) para continuar ou (2) para sair \n')
            quantidade = input('Entre com a nova quantidade1')
        produto = {"Nome:": nome,"quantidade:": quantidade} 
        escolha = input ('digite(1) para continuar editando ou (2) para sair  ')
        while escolha != str(1) and escolha != str(2):
            print('Entre com uma opcao valida : \n')
            escolha = input('digite(1) para continuar editando ou (2)')
        estoquelist.append(produto) 
        contador = 0
       

        for contador in range (0,len(estoquelist)):

            estoque.write(str(num_lines+1)+';' + str(estoquelist[contador]['Nome:']) + ';' + str(estoquelist[contador]['quantidade:']) + '\n')
            num_lines += 1

      
    

add_prod()




def exibir_estoque():
    contador = 0
    estoque = open('estoque.txt','r')
    for i in estoque:
        print(i ,';','\n')
    estoque.close()









