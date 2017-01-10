# -*- encoding: UTF-8 -*-
#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em
#metros quadrados da área a ser pintada. Considere que a cobertura da tinta é
# de 1 litro para cada 3 metros quadrados e que a tinta é vendida em
# de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de
#latas de tinta a serem compradas e o preço total.

metros = int(input("Informe quantidade de metros quadrados: "))

#se 1l de tinta cobre 3 metros, entao 1 lata (com 18l) cobre 54m...logo
if metros <= 54:
    print("precisa apenas de 1 lata. 18L total de R$ 80,00")
else:
    #se precisar de qualquer coisa além de 18L, já é uma segunda lata e por ai vai
    quantidade_de_litros = metros / 3
    if (metros % 3) == 0:
        quantidade_latas_total = quantidade_de_litros / 18
        valor_total = float(quantidade_latas_total * 80)
        print("Precisa de %i latas %iL no total de R$ %.2f" % (quantidade_latas_total, quantidade_de_litros, valor_total))
    else:
        #nesse caso é o número quebrado que sempre vai arredondar pra 1 lata a mais
        quantidade_latas_total = (quantidade_de_litros / 18) + 1
        quantidade_de_litros = quantidade_de_litros + 18
        valor_total = quantidade_latas_total * 80
        print("Precisa de %i latas %iL no total de R$ %.2f" % (quantidade_latas_total, quantidade_de_litros, valor_total))