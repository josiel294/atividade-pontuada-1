import os
os.system("clear")

primeira_unidade = (float(input("Digite sua nota da primeira unidade: ")))
segunda_unidade = (float(input("Digite sua nota da segunda unidade: ")))

media = (primeira_unidade + segunda_unidade) / 2

if media >= 6:
    print("Aprovado")
if media > 4 < 6:
    print("Recuperação")

else:
    print("reprovado")
    
print(f"Media: {media}")
print(f"Primeira unidade: {primeira_unidade}")
print(f"Segunda unidade: {segunda_unidade}")

