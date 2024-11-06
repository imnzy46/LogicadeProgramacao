contador = 0
soma_total = 0
pedidos = []
valor_pizza = 0
refrigerante = 8
ingredientes_preco = 5

print('-' * 60)
print('Olá, sejam bem-vindos à nossa Pizzaria Five Nights at Freddy')
print('-' * 60)

while True:
    # Perguntar o tamanho da pizza
    tamanho = input('Qual o tamanho da Pizza? (Pequena, Média, Grande): ')
    
    if tamanho.lower() == 'pequena':
        valor_pizza = 20
    elif tamanho.lower() == 'média':
        valor_pizza = 30
    elif tamanho.lower() == 'grande':
        valor_pizza = 40
    else:
        print("Tamanho inválido. Tente novamente.")
        continue
    
    total_pedido = valor_pizza
    adicionar_extras = input('Deseja adicionar ingredientes extras? (sim/não): ')
    
    if adicionar_extras.lower() == 'sim':
        if input('Deseja adicionar calabresa? (sim/não): ').lower() == 'sim':
            total_pedido += ingredientes_preco
        if input('Deseja adicionar mussarela? (sim/não): ').lower() == 'sim':
            total_pedido += ingredientes_preco
        if input('Deseja adicionar tomate? (sim/não): ').lower() == 'sim':
            total_pedido += ingredientes_preco
        if input('Deseja adicionar cebola? (sim/não): ').lower() == 'sim':
            total_pedido += ingredientes_preco
        if input('Deseja adicionar bacon? (sim/não): ').lower() == 'sim':
            total_pedido += ingredientes_preco

    if input('Deseja adicionar refrigerante? (sim/não): ').lower() == 'sim':
        total_pedido += refrigerante

    print(f'O valor total do seu pedido é: R${total_pedido:.2f}')
    
    pedidos.append(total_pedido)
    contador += 1
    
    novo_pedido = input("Deseja fazer um novo pedido? (sim/não): ")
    if novo_pedido.lower() != 'sim':
        break
    
if pedidos:
    pedido_mais_caro = max(pedidos)
    pedido_mais_baixo = min(pedidos)
else:
    pedido_mais_caro = pedido_mais_baixo = 0

print(f'Quantidade de pedidos realizados: {contador}')
print(f'O pedido mais caro foi: R${pedido_mais_caro:.2f}')
print(f'O pedido mais baixo foi: R${pedido_mais_baixo:.2f}')