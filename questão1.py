# Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721
def reverso_numero(numero):
    reverso = 0
    while numero > 0:
        digito = numero % 10
        reverso = (reverso * 10) + digito
        numero = numero // 10
    return reverso

numero = int(input("digite um numero inteiro: "))
print(reverso_numero(numero))
