import os
os.system("clear")

print(""""
================= FORMA DE PAGAMENTO =============
\t     \t\tAté 5Kg \t\tAcima de 5Kg                     
1.morango  \t\tR$ 2,50  \t\tR$ 2,20
2.maçã    \t\tR$ 1,80  \t\tR$ 1,50                          
""")

quantos_macas = (float(input("Digite quantas maçãs deseja: ")))
quantos_morango = (float(input("Digite quantos morangos deseja: ")))

maca = float(2.50)
maca2 = float(2.20)
morango = float(1.80)
morango2 = float(1.50)

if quantos_macas or quantos_morango <5:
    total=(quantos_morango*morango)+(quantos_macas*maca)
    print(f"total: {total}")
elif quantos_macas or quantos_morango >8:
    total=(quantos_morango*morango)+(quantos_macas*maca)
    total_final = (total*0.10)
    print(f"valor total a ser pago: {total_final}")
        