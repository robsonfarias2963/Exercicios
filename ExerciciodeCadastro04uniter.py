cadastrarproduto=[]
cadastradoproduto =[]


# ------------ comeco cadastar produto-----------
def cadastrarproduto(rc):
    print('bem vindo cadastrar produto:')
    print('o rc para cadastrar o produto e:{}'.format(rc))
    nome = input('Digite o nome do Produto:')
    fabricante = input('Digite o nome do Fabricante:')
    valor = input ('digite o valor do Produto:')
    dicionarioproduto = {'rc': rc,
                         'nome':nome,
                         'fabricante':fabricante,
                         'valor':valor}
    cadastradoproduto.append(dicionarioproduto.copy())

# ----------- fim cadastrar produto--------------
def consultarprodutos():
    while True:
        try:
            print('Bem vindo consultar produtos:')
            opConsultar = int(input('Entre com a opcao desejada:\n'
                                    '1-Consultar todos os produtos:\n'
                                    '2-Consultar produtos por codigo:\n'
                                    '3-Consultar produtos por fabricante:\n'
                                    '4-retornar'))
            if opConsultar == 1:
                print('Consultar todos os produtos')
                for cadastro in cadastradoproduto:
                    for key , value in cadastro.items():
                        print('{} : {}'.format(key,value))
            elif opConsultar == 2:
                print('Consultar todos os produtos por codigo')
                entrada = int(input('Digite o rc Desejado '))
                for cadastro in cadastradoproduto:
                    if(cadastro ['rc'] == entrada):
                        for key, value in cadastro.items():
                            print('{} : {}'.format(key,value))
            elif opConsultar == 3:
                print('Consultar produtos por fabricante')
                print('Consultar todos os produtos por codigo')
                entrada=int(input('Digite o  nome Desejado '))
                for cadastro in cadastradoproduto :
                    if (cadastro['nome']==entrada) :
                        for key,value in cadastro.items() :
                            print('{} : {}'.format(key,value))
            elif opConsultar == 4:
                break
            else:
                print('Pare de digitar numeros que nao existe no menu:')
                continue
        except ValueError:
            print('Pare de digitar valores nao inteiros')


    print('bem vindo consultar produtos:')


# ------------ fim consultar produtos------------
def removerproduto():
    print('bem vindo para remover o produto:')
    entrada=int(input('Digite o  rc Desejado '))
    for cadastro in cadastradoproduto:
        if (cadastro['nc']==entrada):
            cadastradoproduto.remove(cadastro)


# --------------comeco do menu----------
print('bem vindo ao programa controle de produtos:')
registroproduto=0



while True :
    try:
        opcao=int(input('Digite a opcao desejada:\n'
                    '1-Cadastrar Produto \n'
                    '2- Consultar Produtos \n'
                    '3- Remover Produto \n'
                    '4- Sair\n'
                    '\n>>'))
        if opcao==1:
            registroproduto=registroproduto+1
            cadastrarproduto(registroproduto)
        elif opcao==2:
            consultarprodutos()
        elif opcao==3:
            removerproduto()
        elif opcao==4:
            print('Programa finalizado')
            break
        else:
                 print('Pare de digitar numeros que nao existem no menu:')
        continue
    except ValueError:
                 print('Pare de digitar numeros inteiros:')
