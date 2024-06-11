# Faça uma função que computa a potência ab para valores a e b(assuma números inteiros) passados por parâmetro (não use o operador **).
def potencia(a, b):
    resultado = 1
    for _ in range(b):
        resultado *= a
    return resultado

base = int(input("digite o valor da base: "))
expoente = int(input("digite o valor do expoente:"))
resultado = potencia(base, expoente)
print(resultado)