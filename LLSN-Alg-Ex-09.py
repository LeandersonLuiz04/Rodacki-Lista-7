import random

def verifica_vencedora(cartela):
    # Verificar linhas
    for linha in cartela.values():
        if sum(linha) == 0:
            return True
    
    # Verificar colunas
    for coluna in range(5):
        soma_coluna = sum(cartela[key][coluna] for key in cartela)
        if soma_coluna == 0:
            return True
    
    # Verificar diagonais
    diagonal_principal = [cartela[key][i] for i, key in enumerate(cartela)]
    diagonal_secundaria = [cartela[key][-(i+1)] for i, key in enumerate(cartela)]
    if sum(diagonal_principal) == 0 or sum(diagonal_secundaria) == 0:
        return True
    
    return False

def cria_cartela():
    B = sorted(random.sample(range(1, 16), 5))
    I = sorted(random.sample(range(16, 31), 5))
    N = sorted(random.sample(range(31, 46), 5))
    G = sorted(random.sample(range(46, 61), 5))
    O = sorted(random.sample(range(61, 71), 5))
   
    dict_bingo = {"B": B, "I": I, "N": N, "G": G, "O": O}
    return dict_bingo

def tabela(cartela):
    s = ""
    s += "------------------------------------\n"
    s += "| B\tI\tN\tG\tO  |\n"
    s += "------------------------------------\n"
    for i in range(5):
        s += "| "
        for key in ["B", "I", "N", "G", "O"]:
            s += str(cartela[key][i]) + "\t"
        s += "|\n"  
    s += "------------------------------------\n"
    return s  

def simula_jogo():
    chamadas = list(range(1, 76))
    random.shuffle(chamadas)
    num_chamadas = 0
    
    while True:
        num_chamadas += 1
        chamada = chamadas.pop()
        print(f"Chamada: {chamada}")
        
        if verifica_vencedora(cartela):
            return num_chamadas
            break

def main():
    num_partidas = 1000
    total_chamadas = 0
    min_chamadas = float('inf')
    max_chamadas = float('-inf')
    
    for _ in range(num_partidas):
        cartela = cria_cartela()
        chamadas_para_vencer = simula_jogo()
        
        total_chamadas += chamadas_para_vencer
        min_chamadas = min(min_chamadas, chamadas_para_vencer)
        max_chamadas = max(max_chamadas, chamadas_para_vencer)
    
    media_chamadas = total_chamadas / num_partidas
    
    print(f"Número mínimo de chamadas para vencer: {min_chamadas}")
    print(f"Número máximo de chamadas para vencer: {max_chamadas}")
    print(f"Média de chamadas para vencer: {media_chamadas}")

if __name__=="__main__":
    main()
