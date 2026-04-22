def calcular_area(base, altura):
    area = (base * altura)
    return area


base = float(input("Entre com o valor da base : "))

altura = float(input("Entre com o valor da altura : "))

area = calcular_area(base, altura)

print(f"A área do retângulo é: {area}")