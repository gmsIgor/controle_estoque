def edit_prod():
    #função que exclui ou altera a quantidade de  um produto, ou muda nome.

estoque = open ('estoque.txt','r+')

estoque.seek(0,0)

produtos_list = []

estoque_string = estoque.readlines()

for line in estoque_string :

  line = line[:-1]

  linha = line.split(';')

  produtos_list.append(linha)

print(produtos_list)

produto = input('Entre com o produto que deseja editar : \n')


for contador in range (0,len(produtos_list)) :

  if produtos_list[contador][0] == produto :
    
    print('Entre com 1 para excluir,2 para alterar a quantidade ou 3 para renomear.\n')
    
    escolha =int(input())

    if escolha == 1:

      produtos_list.pop(contador)

    if escolha == 2:

      print('Entre com a nova quantidade do produto : ')
      quantidade = input()
      produtos_list[contador][1] = quantidade
    if escolha == 3 :

        novo_nome=input('Entre com o novo nome :\n')
        produtos_list[contador][0] =  novo_nome
    break



estoque.close()


estoque = open ('estoque.txt','w')

contador = 0

for contador in range (0,len(produtos_list)) :

  estoque.writelines(str(produtos_list[contador][0]) + ';'+ str(produtos_list[contador][1])+'\n')

estoque.close()





# função para procurar o  item no estoque , evitando que alguem tente editar um produto que não está no estoque.

def procura_prod(produto)

estoque = open ('estoque.txt','r+')

estoque.seek(0,0)

produtos_list = []

estoque_string = estoque.readlines()

for line in estoque_string :

  line = line[:-1]

  linha = line.split(';')

  produtos_list.append(linha)

#Esse função pode ser separada pois é necessário transformar em lista para fzer as alterações, vou colocar ela logo em seguida.

contador = 0
produto-em_estoque = 0
for contador in range (0,len(produtos_list)):
# Esse produto será um input do produto que deseja procurar.
    if produtos_list[contador][0] == produto :

        print('Produto está no estoque') #ou nem precisa disso kk
        
        produto_em_estoque = 1
        
        return 1

        break

if produto_em_estoque == 0 :

    print('Produto não se encontra no estoque')

    return 0

#A função retorna 1 se estiver no estoque e 0 caso não esteja.
....................................................................................................................
#função que transforma o arquivo numa lista :

def cria_lista(arquivo) #Nem sei se esse argumento é necessario, vejam ai.


estoque = open ('estoque.txt','r+')

estoque.seek(0,0)

produtos_list = []

estoque_string = estoque.readlines()

for line in estoque_string :

  line = line[:-1]

  linha = line.split(';')

  produtos_list.append(linha)

