num =  soma = 0
while True:
    num = int(input("Digite um numero:"))
    if num == 999:
        break
    soma += num
print(f"A soma vale {soma}")
