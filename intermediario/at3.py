def qntd(palavra):
    vogais = "aeiouAEIOU"
    contador = 0

    for letra in palavra:
        if letra in vogais:
            contador += 1

    return contador

frase = input("entre com uma frase: ")

resultado = qntd(frase)

print(f"Essa frase contém {resultado} vogais!")