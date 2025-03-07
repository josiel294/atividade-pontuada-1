import os
os.system("clear")

#inserir dados
operacao = (str(input("Digite a operação que deseja: ")))
numero_um = (float(input("Digite o número: ")))
numero_dois = (float(input("Digite o número: ")))

match operacao:
    case "+":
        soma = numero_um + numero_dois
        print(f"Valor do resultado: {soma}")
    case "*": 
        multiplicacao = numero_um * numero_dois
        print(f"Valor do resultado: {multiplicacao}")
    case "-": 
        subtracao = numero_um - numero_dois
        print(f"Valor do resultado: {subtracao}")
    case "/":
        divisao = numero_um / numero_dois
        print(f"Valor do resultado: {divisao}")
    case _:
        print("opção invalida")

#exibir dados
print(f"Primeiro número: {numero_um}")
print(f"Segundo número: {numero_dois}")
print(f"Operação: {operacao}")