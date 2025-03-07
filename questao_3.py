import os
os.system("clear")

#inserir dados
valor_um = (int(input("Digite o primeiro valor: ")))
valor_dois = (int(input("Digite o segundo valor: ")))

if valor_um == valor_dois:
    soma = valor_um + valor_dois
    print(f"Valor da soma: {soma}")
else:
 multiplicacao = valor_um * valor_dois
 print(f"Valor da multiplicação: {multiplicacao}")

print(f"Valor do numero um: {valor_um}")
print(f"Valor do numero dois: {valor_dois}")


