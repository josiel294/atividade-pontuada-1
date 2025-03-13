import os
os.system("clear")

print(""""
================= VALOR DOS COMBUSTIVEÍS =============                    
1.Alcool  \t\tAté 25 litros, desconto 2% por  litro
          \t\tAcima 25 litros, desconto de 4% por litro  
       
2.Gasolina   \t\tAté 25 litros, desconto 3% por  litro
          \t\tAcima 25 litros, desconto de 5% por litro                    
                 
""")

quantidade = (float(input("Digite a quantidade: ")))
tipo_do_combustivel = (input("Digite o tipo do  do combustível na ordem dos numeros do combustível: "))
gasolina = float(6.59)
alcool = float(3.79)

match tipo_do_combustivel:
    case "a":
        if quantidade <25:
            total=(quantidade*tipo_do_combustivel)
            total_final = (total*0.02)
            print(f"total: {total}")
            print("2% de desconto")
        elif quantidade > 25:
            total=(quantidade*tipo_do_combustivel)
            total_final = (total*0.04)
            print(f"total: {total}")
            print("4% de desconto")
    case "g":
        if quantidade >25:
            total=(quantidade*tipo_do_combustivel)
            total_final = (total*0.03)
            print(f"total: {total}")
            print("3% de desconto")
        elif quantidade > 25:
            total=(quantidade*tipo_do_combustivel)
            total_final = (total*0.05)
            print(f"total: {total}")
            print("5% de desconto")

    case _: 
        print("combustivel não encontrado")