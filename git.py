contador = 0
soma_total = 0
pedidos = []
valor_pizza = 0
refrigerante = 8
ingredientes_preco = 5
while True:
    print("olá tudo bom temos pizza pequena de R$20, media de R$30, a grande de R$40 qual vc vai querer?")
    pizza=str(input("insira: "))
    if pizza == pequena:
        valordapizza+20
    if pizza == media:
        valordapizza+30
    if pizza == grande:
        valordapizza+40
    adicional=str=("input"("gosta da pizza mais recheada vc pode adicionar mais ums ingrediente? clt1/clt2:"))
    if adicional == clt1:
         print("cada ingrediente é R$5,temos calabresa,mussarela,tomate,cebola e banco")
         while True:
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
            total_pedido+=ingredientes_preco

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


















list
print("caro")
print("barato")
print("pedidos")
print("valordapizza")
print("valordapizza+barato+caro+pedidos")
