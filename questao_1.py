import os 
os.system("clear")

#inserir dados

numero_um = (int(input("digite o primeiro numero: ")))
numero_dois = (int(input("digite o segundo numero: ")))
numero_tres = (int(input("digite o terceiro numero: ")))

soma = numero_um + numero_dois
if soma > numero_tres:
    print("primeiro numero e segundo maior que o terceiro numero")
else:
    print("tereceiro numero maior quê um e dois")
#exibir dados
print(f"numero um escolhido: {numero_um}")
print(f"numero dois escolhido: {numero_dois}")
print(f"numero três escolhido: {numero_tres}")