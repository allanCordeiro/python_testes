# -*- encoding: UTF-8 -*-
#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a
#velocidade de um link de Internet (em Mbps), calcule e informe o tempo
#aproximado de download do arquivo usando este link (em minutos).

tamanho_arquivo = int(input("Tamanho do arquivo (em MB): "))
velocidade_internet = int(input("Link de internet (em Mbps)"))

tamanho_convertido = tamanho_arquivo * 8
velocidade_em_segundos = tamanho_convertido / velocidade_internet
velocidade_em_minutos = float(velocidade_em_segundos / 60)
print("velocidade em minutos do download: %.2f" % velocidade_em_minutos)