# pedido = ['mouse', 'teclado', 'monitor']
# contador = 0
# chave = 'teste'

# while input('Descubra a palavra: ') != chave:
#     print("Ops que pena errou")


# for produto in pedido:
#     if(produto == 'teclado'):
#         pass
        
#     print(produto)    

# # texto  = input('Digite aqui:   ')
# # print(texto)

# listaDeCompras = {
#     'pao': 10,
#     'café': 50,
#     'arroz': 30
# }
# total = 0

# for produto, preco in listaDeCompras.items():
#     total = preco + preco 

# print("Total da compra: " + str(total))


# produts = ['teclado', 'mouse', 'abacate']

# for product in produts:
#     print(product)


# print('deu certo')    

# caixa = 0
# precoPelucia = 50

# while caixa < precoPelucia:
#     valorInserido = input('Digite um valor: ')
#     caixa = float(caixa) + float(valorInserido)
    
# print('Voce ganhou uma pelucia')    

carrinho = [
    {"produto": "Arroz", "preco": 10.00},
    {"produto": "feijao", "preco": 15.00},
    {"produto": "Pão", "preco": 25.00},
    {"produto": "Pera", "preco": 5.00},
]

total = 0

for item in carrinho:
    total = total + item["preco"]

print(total)


# carrinho = [
#     {"produto": "cafe", "preco": 30.00},
#     {"produto": "pão", "preco": 50.00},
#     {"produto": "abacate", "preco": 10.00}
# ]

# total = 0

# for item in carrinho:
#     total += item["preco"]

# print("Total da compra: " + str(total)) 