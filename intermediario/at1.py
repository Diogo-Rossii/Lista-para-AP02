valor = []

while True: 
    entrada = input("Entre com um valor(PARA SAIR BASTA ENVIAR VAZIO): ")

    if entrada == "":
        break

    numero = float(entrada)
    valor.append(numero)

def media(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

resultado = media(valor)

print(f"A media dos valores é: {resultado:.2f}")

