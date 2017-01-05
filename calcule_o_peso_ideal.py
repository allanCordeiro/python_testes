# -*- coding: UTF-8 -*-
#Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um
#algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7
# sendo que(h = altura)
#Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso.

sexo = raw_input("Qual seu gênero [M/F]: ")
altura = float(input("Altura em metros: "))
peso = float(input("Seu peso em KG: "))

if sexo == "M":
    peso_ideal = float(format((72.7 * altura) - 58, ".1f"))
    #please somebody helpme!! :)
    if peso == peso_ideal:
        print("Você está no peso. Parabéns")
    if peso > peso_ideal:
        print("Você está acima do peso. Seu peso ideal deveria ser %.1f" % peso_ideal)
    elif peso < peso_ideal:
        print("Você está abaixo do peso. Seu peso ideal deveria ser %.1f" % peso_ideal)
elif sexo == "F":
    peso_ideal = float(format((62.1 * altura) - 44.7, ".1f"))
    if peso > peso_ideal:
        print("Você está acima do peso. Seu peso ideal deveria ser %.1f" % peso_ideal)
    elif peso < peso_ideal:
        print("Você está abaixo do peso. Seu peso ideal deveria ser %.1f" % peso_ideal)
    elif peso == peso_ideal:
        print("Você está no peso. Parabéns")