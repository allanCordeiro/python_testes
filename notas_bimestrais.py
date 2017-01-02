#Faca um Programa que peca as 4 notas bimestrais e mostre a media.
print("Voce vai colocar suas notas aqui e teremos a media")
pri_bimestre = float(input("Nota do primeiro bimestre: "))
seg_bimestre = float(input("Nota do segundo bimestre: "))
ter_bimestre = float(input("Nota do terceiro bimestre: "))
qua_bimestre = float(input("Nota do quarto bimestre: "))

nota_final = (pri_bimestre + seg_bimestre + ter_bimestre + qua_bimestre) / 4
print("Sua nota de fim de ano foi %.2f" % nota_final)