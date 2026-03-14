# Exercício 2 – Área e Perímetro do Quadrado
# Faça um algoritmo que:
# Leia o valor do lado de um quadrado.
# Calcule:
# a área
# o perímetro
# Exiba os resultados.
# Fórmulas:
# Área = lado × lado
# Perímetro = 4 × lado

ladoEmTexto = input("Digite o lado do quadrado: ")
lado = float(ladoEmTexto)

area = lado * lado
perimetro = 4 * lado


print("a área é ")
print(area)
print("\n\n") # \n  significa enter
print("o perimetro é ")
print(perimetro)