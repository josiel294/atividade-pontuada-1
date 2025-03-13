import os
os.system ("clear")

# Preços dos combustíveis
preco_gasolina = 6.59
preco_alcool = 3.79

# Leitura dos dados
litros = float(input("Digite o número de litros vendidos: "))
tipo_combustivel = input("Digite o tipo de combustível (A-álcool, G-gasolina): ").upper()

# Cálculo e aplicação de desconto
if tipo_combustivel == 'A':
    if litros <= 25:
        # Desconto de 2% por litro
        preco_com_desconto = preco_alcool * 0.98
    else:
        # Desconto de 4% por litro
        preco_com_desconto = preco_alcool * 0.96
    valor = litros * preco_com_desconto
    print(f"O valor a ser pago pelo cliente pelo álcool é: R$ {valor:.2f}")

elif tipo_combustivel == 'G':
    if litros <= 25:
        # Desconto de 3% por litro
        preco_com_desconto = preco_gasolina * 0.97
    else:
        # Desconto de 5% por litro
        preco_com_desconto = preco_gasolina * 0.95
    valor = litros * preco_com_desconto
    print(f"O valor a ser pago pelo cliente pela gasolina é: R$ {valor:.2f}")

else:
    print("Tipo de combustível inválido. Por favor, digite 'A' para álcool ou 'G' para gasolina.")
