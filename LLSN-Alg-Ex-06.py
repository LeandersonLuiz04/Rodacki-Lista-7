

def limpar_texto(txt):
    txt_limpo = ''.join(char.lower() for char in txt if char.isalnum())
    return txt_limpo

def anagrama():
    txt1 = input("Frase 1: ")
    txt2 = input("Frase 2: ")
    txt1_limpo = limpar_texto(txt1)
    txt2_limpo = limpar_texto(txt2)

    if sorted(txt1_limpo) == sorted(txt2_limpo):
        print("São anagramas")
    else:
        print("Não são anagramas")

anagrama()
