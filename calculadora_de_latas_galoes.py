# -*- encoding: UTF-8 -*-
#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em
#metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de
# 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos
#preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e
# arredonde os valores para cima, isto é, considere latas cheias.

quantidade_metros = int(input("Informe quantidade de metros: "))
quantidade_litros = quantidade_metros / 6
arredondamento = quantidade_litros + (quantidade_litros * 0.1)
#preciso entender se a proporção inicial é maior de 18L
proporcao_18 = arredondamento / 18
proporcao_3_6 = arredondamento / 3.6
latas_18 = 0
latas_3_6 = 0
litros = 0
litros_faltantes = 0
while litros < arredondamento:
    if proporcao_18 >= 1:
        latas_redondas = int(proporcao_18)
        proporcao_18 = proporcao_18 - latas_redondas
        litros = litros + (latas_redondas * 18)
        latas_18 = latas_18 + latas_redondas
    else:
        if litros_faltantes == 0:
            litros_faltantes = arredondamento - litros
        if (litros_faltantes / 3.6) < 1:
            #se mesmo assim  não o fechar o galão, terá de 1 comprar inteiro
            latas_3_6 = latas_3_6 + 1
            litros = litros + 3.6
        else:
            #é só o resto, pega e soma + 1
            latas_3_6 = latas_3_6 + 1
            litros_faltantes = litros_faltantes - 3.6
            litros = litros + 3.6

#agora é só exibir o valor de latas e o valor final
valor_lata = latas_18 * 80.00
valor_galao = latas_3_6 * 25.00
#se tiver 3 galoes, ocorre a conversao pra 1 de 18 por causa do preço
redimensionou = 0
if valor_galao > 75.00:
    valor_lata = valor_lata + 80.00
    valor_galao = valor_galao - 75.00
    latas_18 = latas_18 + 1
    latas_3_6 = latas_3_6 - 3
    redimensionou = 1

print("Total de latas: %d" % latas_18)
print("Total de galões: %d" % latas_3_6)
print("Valor de R$ %.2f de lata(s) e R$ %.2f de galões, total de R$ % .2f" % (valor_lata, valor_galao, valor_lata + valor_galao))
if redimensionou == 1:
    print("Na conta, 4 galões foram substituídos por 1 lata de 18L por reduzir o valor final")
