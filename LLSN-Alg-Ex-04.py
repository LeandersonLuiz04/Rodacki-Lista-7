logo='''
╔═╗┌─┐┌┬┐┬┌─┐┌─┐  ╔╦╗┌─┐┬─┐┌─┐┌─┐
║  │ │ ││││ ┬│ │  ║║║│ │├┬┘└─┐├┤ 
╚═╝└─┘─┴┘┴└─┘└─┘  ╩ ╩└─┘┴└─└─┘└─┘
'''
print(logo)
print("AVISO: A decodificação deste código pode apresentar erros, peço desculpas!!!")

morse={


"A":".-",
"B":"-...",
"C":"-.-.",
"D":"-..",
"E":".",
"F":"..-.",
"G":"- -.",
"H":"....",
"I":"..",
"J":".- - -",
"K":"-.-",
"L":".-..",
"M":"- -",
"N":"-.",
"O":"---",
"P":".- -.",
"Q":"- -.-",
"R":".-.",
"S":"...",
"T":"-",
"U":"..-",
"V":"...-",
"W":".- -",
"X":"-..-",
"Y":"-.- -",
"Z":"- -..",
"0":"-----",
"1":".- - - -",
"2":"..- - -",
"3":"...- -",
"4":"....-",
"5":".....",
"6":"-....",
"7":"- -...",
"8":"- - -..",
"9":"- - - -.",


}
decodificar={


".-":"A",
"-...":"B",
"-.-.":"C",
"-..":"D",
".":"E",
"..-.":"F",
"- -.":"G",
"....":"H",
"..":"I",
".- - -":"J",
"-.-":"K",
".-..":"L",
"- -":"M",
"-.":"N",
"---":"O",
".--.":"P",
"- -.-":"Q",
".-.":"R",
"...":"S",
"-":"T",
"..-":"U",
"...-":"V",
".--":"W",
"-..-":"X",
"-.- -":"Y",
"- -..":"Z",
"-----":"0",
".- - - -":"1",
"..- - -":"2",
"...- -":"3",
"....-":"4",
".....":"5",
"-....":"6",
"- -...":"7",
"- - -..":"8",
"- - - -.":"9",


}


choice=input("Digite C para codificar e D para decodificar: ").upper()


texto_codificado=[]
texto_decodificado=[]


if choice=="C":
    mensagem=input("TEXTO: ").upper()
    mensagem=mensagem.replace(" ","")


    for i in mensagem:
        m=morse[i]
        texto_codificado.append(m)
        texto_codificado.append(" ")


    txt= "".join(map(str,texto_codificado))
   
    print(f"MENSAGEM EM CÓDIGO MORSE: {txt}")


elif choice == "D":
    mensagem = input("TEXTO: ")
    texto = mensagem.split()
    print(texto)

    for i in texto:
        if i in decodificar: 
            m = decodificar[i]
            texto_decodificado.append(m)
        else:
            texto_decodificado.append("?") 

    txt = "".join(map(str, texto_decodificado))

    print(f"MENSAGEM DECODIFICADA: {txt}")






