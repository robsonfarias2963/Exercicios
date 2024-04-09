def operar(x,y=2) :
    valor=3
    for i in range(y) :
        valor=valor*x
    return valor


print(operar(4))
print(operar(4,4))
