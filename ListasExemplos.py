equipamentos = []
valores = []
serias = []
departamentos = []
resposta = "S"
while resposta =="S":
    equipamentos.append(input('Equipamento: '))
    valores.append(float(input("Valor: ")))
    serias.append(int(input("Numero Serial :")))
    departamentos.append(input('Departamento:'))
    resposta = input("Digite \"S\" para continuar :").upper()

for equipamento in equipamentos:
    print("Equipamento",equipamento)
