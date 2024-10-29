numero = int(input("Digite um número inteiro: "))
eh_primo = numero > 1 and all(numero % i != 0 for i in range(2, int(numero**0.5) + 1))

if eh_primo:
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")