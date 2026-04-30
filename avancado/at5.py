def mais_caro(produtos):
    if not produtos:
        return None
    mais_caro_produto = produtos[0]
    for produto in produtos:
        if produto['preco'] > mais_caro_produto['preco']:
            mais_caro_produto = produto
    return mais_caro_produto 

# Exemplo de uso
produtos = [
    {'nome': 'Produto A', 'preco': 10.0},
    {'nome': 'Produto B', 'preco': 20.0},
    {'nome': 'Produto C', 'preco': 15.0}
]
print(mais_caro(produtos))


