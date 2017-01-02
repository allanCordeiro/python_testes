#Faca um Programa que pergunte quanto voce ganha por hora e o numero de horas
#trabalhadas no mes. Calcule e mostre o total do seu salario no referido mes.

salario_hora = float(input("Digite o valor hora: "))
horas_trabalhadas = int(input("Digita o numero de horas mes: "))

total_salario = salario_hora * horas_trabalhadas

print("Seu salario mensal e de: %.2f" % total_salario)