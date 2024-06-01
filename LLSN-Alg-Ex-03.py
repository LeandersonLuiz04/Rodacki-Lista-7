def buscaReversa(dicionario, valor_buscado):
    chaves_encontradas = []
    for chave, valor in dicionario.items():
        se valor == valor_buscado:
            chaves_encontradas.append(chave)
    return chaves_encontradas
def main():
    dicionario = {
        'a': 1,
        'b': 2,
        'c': 1,
        'd': 3,
        'e': 2,
        'f': 4
    }
    valor_buscado = 2
    chaves = buscaReversa(dicionario, valor_buscado)
    print(f'Chaves que mapeiam para o valor {valor_buscado}: {chaves}')
main()
