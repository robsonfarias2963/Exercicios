def solicitar_nome():
    return str ( input("Digite um nome: ") )

def adicionar_nome_na_lista(lista, nome):
    lista.append(nome)

def escrever_nomes(lista):
    for nome in lista:
        print(nome)

nomes = []
for contador in range(0,5):
    nome = solicitar_nome()
    adicionar_nome_na_lista(nomes, nome)

escrever_nomes(nomes)