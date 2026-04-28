def fatorial(n):
    if n == 0:
        return 1
   
    resultado = 1
    while n > 0:
        resultado *= n
        n -= 1

    return resultado

print(fatorial(5))