def sao_anagramas(palavra1, palavra2):
    if len(palavra1) != len(palavra2):
        return False
    return sorted(palavra1) == sorted(palavra2)
print(sao_anagramas("amor", "roma")) #retorna True

