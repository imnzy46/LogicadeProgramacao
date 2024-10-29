maior_altura = 0
menor_altura = float('inf')
aluno_mais_alto = aluno_mais_baixo = 0

for _ in range(10):
    numero_aluno, altura = map(int, input("Digite o número do aluno e a altura em cm: ").split())
    if altura > maior_altura:
        maior_altura, aluno_mais_alto = altura, numero_aluno
    if altura < menor_altura:
        menor_altura, aluno_mais_baixo = altura, numero_aluno

print(f"Aluno mais alto: {aluno_mais_alto} com {maior_altura} cm.")
print(f"Aluno mais baixo: {aluno_mais_baixo} com {menor_altura} cm.")