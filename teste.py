def editar_prod():
    estoque = open ('estoque.txt','r+')

    estoque.seek(0,0)

    produtos_list = []

    estoque_string = estoque.readlines()

    for line in estoque_string :

        line = line[:-1]

        linha = line.split(';') 

        produtos_list.append(linha)
        




    print(produtos_list)



    produto = input('Entre com o produto : \n')
    for contador in range (0,len(produtos_list)) :
    
        if produtos_list[contador][0] == produto :

            linha_produto = contador 

            print ('O produto esta na linha' + '\t' + str(contador))
    
            
    
    linha_remove = int(input('Entre com a linha que deseja excluir\n'))
    produtos_list.pop(linha_remove)
    estoque= open('estoquenovo.txt','w')
    estoque.writelines(str(produtos_list))
    print(produtos_list)
    estoque.close()












def editar_prod2():
    estoque = open('estoque.txt','r+')
    estoque_string = estoque.readlines()
    estoque.seek(0,0)
    
    for line in estoque_string:
        line = line[:-1]
        linha = line.split(';')
        cont = 0
        for cont in range(0,len(estoque_string)):
            Nome =linha[0]
            Quantidade = linha[1]
            
            cont +=1
    
        produto = {'Nome:':Nome,'Quantidade:':Quantidade}
    print (produto)
editar_prod2()