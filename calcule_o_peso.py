# -*- coding: UTF-8 -*-
#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que
#calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input("Coloque sua altura em metros: "))
peso_ideal = (72.7 *  altura) - 58

print("seu peso ideal é de %.1f quilos." % peso_ideal)
