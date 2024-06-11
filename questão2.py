#Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado. 
def contar_digitos(numero):
    return len(str(numero))


numero = int(input("digite um numero inteiro: "))
quantidade_digitos = contar_digitos(numero)
print(quantidade_digitos)

