from random import randint
def Craps():
    jogar_primeira = input('Pressione Enter para jogar: ')
    if jogar_primeira == '':
        while True:
            numero_jogado = randint(2, 12)
            if numero_jogado >= 4 and numero_jogado <= 10 and numero_jogado != 7 and numero_jogado != 11:
                ponto = numero_jogado
                print(f'O seu ponto é {ponto}')
                break
            elif numero_jogado == 7 or numero_jogado == 11:
                ponto = numero_jogado
                print(numero_jogado)
                print(f'Voce ganhou')
                quit()
            elif numero_jogado == 2 or numero_jogado == 3 or numero_jogado == 12:
                ponto = numero_jogado
                print(numero_jogado)
                print('Craps!! Voce perdeu')
                quit()
            numero_jogado = 0

    novo_ponto = 0
    qtd_jogadas = 0
    while novo_ponto != ponto:
        print('-' * 30)
        jogadas = input('Pressione Enter para jogar: ')
        if jogadas == '':
            numero_jogado = randint(2, 12)
            print('O numero é:')
            print(numero_jogado)
            if numero_jogado == ponto:
                novo_ponto = ponto 
                print('Voce encontrou o ponto correto. Ganhou!!!')
                break
            if numero_jogado == 7:
                print('Voce perdeu')
                break
            else:
                numero_jogado = 0 
                qtd_jogadas += 1
                continue
    print(f'Voce jogou {qtd_jogadas} vezes')


while True:
    jogar = input('Vamos jogar? [S/N] ')
    jogar = jogar.upper()
    if jogar == 'S':
        Craps()
    else:
        break