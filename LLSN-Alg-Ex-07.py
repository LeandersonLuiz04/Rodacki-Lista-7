logo='''

┳┓•      
┣┫┓┏┓┏┓┏┓
┻┛┗┛┗┗┫┗┛
      ┛  

'''
import random
print(logo)


dict_bingo={
    "B":1,
    "I":2,
    "N":3,
    "G":4,
    "O":5,
}


def cria_cartela():


    dict_bingo = dict()


    B=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    I=[16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    N=[31,32,33,34,35,36,37,38,39,40,41,42,43,44,45]
    G=[46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]
    O=[61,62,63,64,65,66,67,68,69,70]
   
    valores_B=random.sample(B,5)
    valores_I=random.sample(I,5)
    valores_N=random.sample(N,5)
    valores_G=random.sample(G,5)
    valores_O=random.sample(O,5)
   
   
    dict_bingo["B"]=sorted(valores_B)
    dict_bingo["I"]=sorted(valores_I)
    dict_bingo["N"]=sorted(valores_N)
    dict_bingo["G"]=sorted(valores_G)
    dict_bingo["O"]=sorted(valores_O)


    return dict_bingo


def tabela(dict_bingo):
    s = ""
    s += "------------------------------------\n"
    s += "| B\tI\tN\tG\tO  |\n"
    s += "------------------------------------\n"
    for i in range(5):
        s += "| "
        s += str(dict_bingo["B"][i]) + "\t"
        s += str(dict_bingo["I"][i]) + "\t"
        s += str(dict_bingo["N"][i]) + "\t"
        s += str(dict_bingo["G"][i]) + "\t"
        s += str(dict_bingo["O"][i]) + " |\n"  
    s += "------------------------------------\n"
    return s  

def main():
    cartela = cria_cartela()
    cartela_formatada = tabela(cartela)
    print(cartela_formatada)


if __name__=="__main__":
    main()


