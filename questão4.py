# faça um programa que tenha uma funçao chamada maior(), que receba vários parametros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é maior.


def maior(*numeros):
    maior_num = numeros[0]
    for numero in numeros:
        if numero > maior_num:
            maior_num = numero
    print(maior_num)

maior(1, 2, 3)
 
