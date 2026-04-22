def verificarpar(numero):
    if numero % 2 == 0:
        return ("O numero é par")
    else:
        return ("O numero é impar")
    

numero = int(input("Entre com um numero:"))

print(verificarpar(numero))