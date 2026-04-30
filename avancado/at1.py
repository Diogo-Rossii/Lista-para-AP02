def leiaint(msg):
    while True:
        n = input(msg)
        if n.isnumeric():
            return int(n)
        print("Erro! Entre com um número inteiro.")

valor = leiaint("Entre com um número inteiro: ")
print(f"O número que você entrou foi {valor}")