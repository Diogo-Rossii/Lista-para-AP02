def maior_valor(a,b):
    if a > b:
        return a
    else:
        return b

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: ")) 

print(f"O numero maior é: {maior_valor(a,b)}")