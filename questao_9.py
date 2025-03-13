import os
os.system ("clear")
#solicitar dados
renda_mensal = (float(input("Digite sua renda mensal: ")))
valor_emprestimo = (float(input("Digite o valor do emprestimo: ")))
quantidade_prestacoes = (int(input("Digite quantas prestações deseja: ")))

valor_maximo_emprestimo = renda_mensal * 10
prestacao_mensal = valor_emprestimo / quantidade_prestacoes
valor_maximo_prestacoes = renda_mensal * 0.3

#verificar limite pode ser concedido

if valor_emprestimo <= valor_maximo_emprestimo and prestacao_mensal <= valor_maximo_prestacoes:
    print("Emprestimo APROVADO!")
else:
    print("Emprestimo REPROVADO!")

