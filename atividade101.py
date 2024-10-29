#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

n=0
i=str(input("informe se voce é homem ou mulher: "))
h=float(input("informe sua altura: "))

if i=='ho':
    n=(72.7*h)-58
    print(n)

if i=='m':
    n=(62.1*h)-44.7
    print (n)