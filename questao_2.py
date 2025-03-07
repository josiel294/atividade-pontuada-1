import os
os.system("clear")
#inserir dados
dados = 0
estado_civil = (str(input("Digite seu estado civíl: " ).lower))
sexo = (str(input("Digite seu sexo: ").lower))
if estado_civil == "casada":
 dados = (str(input("Digite quanto tempo de casada possui: ")))
else:
 print("Muito obrigado por sua informação")

 #exibir dados

 print(f"Estado civíl: {estado_civil}")
 print(f"Sexo: {sexo}")
 print(f"Dados pessoais: {dados}")

 