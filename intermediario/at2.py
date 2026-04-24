def convertor (c):
    fa = (c * 1.8) + 32
    return fa

c_usuario = int(input("Entre com um °C: "))

resultado = convertor(c_usuario)

print(f"A temperatura é: {resultado}°F")