##Exercício simulando uma fatura.

fatura = []
total = 0
continuar = 's'
valid_preco = False

while continuar == 's':
    prod = input("Digite o nome do produto: ")

    while valid_preco == False: ##Este While faz a conversão do preço para float através do Try.
        preco = input("Digite o valor do produto: ")
        try:
            preco = float(preco)
            if preco <= 0:
                print ("O preço necessita ser maior que zero")
            else:
                valid_preco = True

        except: ## Caso não consiga converter, como por exemplo o usuário digitar um texto, dará a mensagem abaixo.
            print ("Formato de preço inválido. Use apenas números e separe os centavo com '.'.")

    fatura.append([prod, preco])
    total += preco
    valid_preco = False
    continuar = input("Deseja comprar algo mais? Por favor, digite S para sim e N para não: ").lower()

for i in fatura:
    print (i[0], ':', i[1])
print ('O total da fatura é: ', total)
