print('Sequência de Fibonacci\n')
# leitura do número de termos
N = 0
while N < 2:
    try:
        N = int(input('Digite N(>1): '))
        if N < 2:
                print('Digite N >= 2')
    except:
        print('O dado digitado deve ser um número inteiro.')
# criação da lista com a sequência de Fibonacci
L = [0, 1]
for i in range(N-2):
    L.append(L[i] + L[i+1])
print('Sequência gerada:', L)
print('Fim do Programa')