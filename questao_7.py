import os
os.system("clear")


quantos_peixes = (float(input("Digite quantas maçãs deseja: ")))
quantos_carangueijo = (float(input("Digite quantos morangos deseja: ")))

peixes = float(59.90)
peixes2 = float(56.65)
carangueijo = float(32.80)
carangueijo2 = float(28.50)

if quantos_peixes or quantos_carangueijo <=5:
    total=(quantos_carangueijo*carangueijo)+(quantos_peixes*peixes)
    total_final = (total*0.02)
    print(f"total: {total}")
    print("2% de desconto")
elif quantos_peixes or quantos_carangueijo >5 <= 10:
    total=(quantos_carangueijo*carangueijo)+(quantos_peixes*peixes)
    total_final = (total*0.03)
    print(f"valor total a ser pago: {total_final}")
    print("3% de desconto")
elif quantos_peixes or quantos_carangueijo >10:
    total=(quantos_carangueijo*carangueijo)+(quantos_peixes*peixes)
    total_final = (total*0.05)
    print(f"valor total a ser pago: {total_final}")
    print("5% de desconto")
        