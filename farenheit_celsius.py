#Faca um Programa que peca a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
#formula C = (5 * (F-32) / 9).

temperatura_farenheit = float(input("digite a temperatura em Celsius: "))

temperatura_celsius = (5 * (temperatura_farenheit - 32) / 9)
print("A tempetura em celsius eh de: %.1f" % temperatura_celsius)