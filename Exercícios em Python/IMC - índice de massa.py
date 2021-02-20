## calculo imc: peso/(altura*altura)

def imc (peso, altura):
    imc = peso/(altura*altura)
    return(imc)
def classif (genero, peso, altura):
    valor_imc = imc(peso, altura)
    if genero == 'm' or genero == 'M':
        if valor_imc < 19.1:
            return "Abaixo do peso"
        elif valor_imc >= 19.1 and valor_imc <= 25.8:
            return "Peso ideal"
        elif valor_imc >= 25.8 and valor_imc <= 27.3:
            return "Um pouco acima do peso."
        elif valor_imc >= 27.3 and valor_imc <= 32.3:
            return "Acima do peso."
        elif valor_imc > 32.3:
            return "Obeso."
        else:
            return "Erro de cálculo. Contate o administrador."
    if genero == 'h' or genero == 'H':
        if valor_imc < 20.7:
            return "Abaixo do peso"
        elif valor_imc >= 20.7 and valor_imc < 26.4:
            return "Peso ideal"
        elif valor_imc >= 26.4 and valor_imc < 27.8:
            return "Um pouco acima do peso."
        elif valor_imc >= 27.8 and valor_imc < 31.1:
            return "Acima do peso."
        elif valor_imc > 31.1:
            return "Obeso."
        else:
            return "Erro de cálculo. Contate o administrador."
valid_genero = False
valid_pesoalt = False

while valid_pesoalt == False:
    peso = input("Informe seu peso: ")
    try:
        peso = float(peso)
        if peso < 0:
            print ("O peso necessita ser maior que zero. Verifique os dados inseridos: ")
        else:
            valid_pesoalt = True
    except:
        print ("Formato inválido. Digite '.' para separar as gramas.")
valid_pesoalt = False
while valid_pesoalt == False:
    altura = input("Informe sua altura: ")
    try:
        altura = float(altura)
        if altura < 0:
            print ("A altura necessita ser maior que zero. Verifique os dados inseridos: ")
        else:
            valid_pesoalt = True
    except:
        print ("Formato inválido. Digite '.' para separar os CM.")
valid_pesoalt = False
while valid_genero == False:
    genero = input("Informe seu genero, sendo H para homem e M para mulher: ").lower()
    if genero != 'm' and genero != 'h':
        print ("Digite apenas H para homem e M para mulher. Verifique os dados inseridos.: ")
    else:
        valid_genero = True
valid_genero = False

#Nas duas variáveis abaixo chamamos as funções que determinamos anteriormente.
v_imc = imc (peso, altura)
c_imc = classif (genero, peso, altura)

print ("Seu IMC é: ", v_imc)
print ("Sua classificação é: ", c_imc)