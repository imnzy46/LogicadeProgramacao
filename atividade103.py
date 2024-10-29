nome = input("Nome (mais que 3 caracteres): ")
while len(nome) <= 3: nome = input("Inválido. Digite novamente: ")

idade = int(input("Idade (0 a 150): "))
while idade < 0 or idade > 150: idade = int(input("Inválido. Digite novamente: "))

salario = float(input("Salário (maior que zero): "))
while salario <= 0: salario = float(input("Inválido. Digite novamente: "))

sexo = input("Sexo (f ou m): ").lower()
while sexo not in ['mulher', 'homem']: sexo = input("Inválido. Digite novamente: ").lower()

estado_civil = input("Estado civil (s, c, v, d): ").lower()
while estado_civil not in ['s', 'c', 'v', 'd']: estado_civil = input("Inválido. Digite novamente: ").lower()
