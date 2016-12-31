#vi isso em algum forum
#algum professor de programacao passou este exercicio em alguma linguagem X
#estou replicando-a em python

#vagabundo=somatorio(mes)+(ano/100)*(50-dia)
#anjo = 100 - safadeza

dia = int(input("informe dia de nascimento: "))
mes = int(input("informe mes de nascimento: "))
ano = int(input("informe ano de nascimento: "))

vagabundo = mes + (ano/100) * (50-dia)
anjo = 100 - vagabundo
print("Voce eh %d%% anjo, mas %d%% vagabundo" %(vagabundo, anjo))