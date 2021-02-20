valid_nota = False
valid_faltas = False
valid_nome = False

while valid_nome == False:
    nome = input('Digite o nome do aluno(a): ')
    try:
        nome = str(nome)
        if nome.isdigit():
            print ("Formato inválido. Digite somente letras.")
        else:
            valid_nome = True
    except:
        print ("Formato inválido. Digite apenas letras")
valid_nome = False

while valid_nota == False:
    n1 = input('Digite a nota da 1ª prova: ')
    try:
        n1 = float(n1)
        if n1 < 0 or n1 > 10:
            print("A nota necessita ser de 0 a 10. Verifique o valor inserido.")
        else:
            valid_nota = True
    except:  ## Caso não consiga converter, como por exemplo o usuário digitar um texto, dará a mensagem abaixo.
        print("Formato inválido. Verifique os dados inseridos.")

valid_nota = False
while valid_nota == False:
    n2 = input('Digite a nota da 2ª prova: ')
    try:
        n2 = float(n2)
        if n2 < 0 or n2 > 10:
            print("A nota necessita ser de 0 a 10. Verifique o valor inserido.")
        else:
            valid_nota = True
    except:  ## Caso não consiga converter, como por exemplo o usuário digitar um texto, dará a mensagem abaixo.
        print("Formato inválido. Verifique os dados inseridos.")

while valid_faltas == False:
    faltas = input('Digite o total de faltas do aluno(a): ')
    try:
        faltas = int(faltas)
        if faltas < 0 or faltas > 20:
            print ("As faltas precisam ser entre 0 e 20. Verifique os dados inseridos.")
        else:
            valid_faltas = True
    except:
        print ("Formato inválido. Verifique os dados inseridos.")

assid = (20-faltas)/20
media = (n1+n2)/2

if media >= 6 and assid >= 0.7:
    resultado = 'Aprovado'
elif media < 6 and assid < 0.7:
    resultado = 'Reprovado por média e por falta.'
elif media < 6:
    resultado = 'Reprovado por média'
elif assid < 0.7:
    resultado = 'Reprovado por falta'
else:
    print ('Erro. Verifique os dados inseridos.')

print('Nome:', nome)
print('Média:', media)
print('Assiduidade:', str(assid*100)+'%')
print('Resultado:', resultado)