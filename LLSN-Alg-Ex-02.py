def diferenca_simetrica(M, N):

    diferenca_sim = M ^ N

    resultado = sorted(list(diferenca_sim))
    return resultado


M = {2, 4, 5, 9}
N = {2, 4, 11, 12}
print(diferenca_simetrica(M, N)) 
