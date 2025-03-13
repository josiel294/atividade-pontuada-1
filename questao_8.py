import os
os.system("clear")

print(""""
================= CORES =============
Cores \t\t\tPreço                    
1.Verde   \t\tR$ 10,00
2.Azul   \t\tR$ 20,00                           
3.Amarelo    \t\tR$ 30,00                          
4.Vermelho    \t\tR$ 40,00                          
""")
#solicitar dados
cor = ((input("Digite a cor que deseja: ").lower))

#verificação de dados
if cor () == "verde":
    print("O preço do CD é R$ 10,00")
elif cor () == "azul":
    print("O preço do CD é R$ 20,00")
elif cor ()== "amarelo":
    print("O preço do CD é R$ 30,00")
elif cor () == "vermelho":
    print("O preço do CD é R$ 40,00")
else:
    print("Cor invalida tente novamente")