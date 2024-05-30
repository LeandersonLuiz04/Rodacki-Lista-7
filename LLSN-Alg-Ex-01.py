def caracteres_unicos(s):
    caracteres_vistos = set()
    for char in s:
        if char in caracteres_vistos:
            return False  
        caracteres_vistos.add(char)
    return True

# exemplo
print(caracteres_unicos("python"))     # vai retornar True

