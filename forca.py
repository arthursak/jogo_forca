def joga_forca():
    
    import random

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    #Define a palavra secreta e cria lista
    num_palavra = random.randrange(0, len(palavras))
    palavra = palavras[num_palavra].upper()
    letras_certas = []

    #Traduz caracteres da lista para ficarem ocultos e dinamico para qualquer palavra
    for letra in palavra:
        letras_certas.append("_")

    print (f"Bem vindo ao jogo da Forca!\nAdivinhe a palavra secreta: {letras_certas}\n")
    
    #Variaveis de finalização de game
    enforcou = False
    acertou = False
    erros = 0

    #Estrutura funcional/ Jogo continua até as variaveis de finalização serem True
    while (not enforcou and not acertou):

        chute = input("Digite uma letra:\n").upper()

        #Verifica se a letra advinhada contem na palavra/ Ccoloca na sua devida posição
        if chute in palavra:
            index = 0
            for letra in palavra:
                if chute == letra:
                    letras_certas [index] = letra
                index += 1
        
        #Adiciona 1 erro caso a letra não esteja na palavra
        else:
            erros += 1

        #Caso a variavel erros chegue a 6, enforcou vira True e o jogo finaliza com derrota
        enforcou = erros == 6

        #Caso não haja mais o caracter oculto, o jogo finaliza com o acertou True
        acertou = "_" not in letras_certas

        if acertou:
            print(f"Você ganhou!\n A palavra era {palavra}")
        else:
            print("Enforcou!")


    print ("Fim do game")

'''
erro1 = print ("/")
erro2 = print ("/ \")
erro3 = print (" | \n/ \")
erro4 = print ("/ | \n/ \")
erro5 = print ("/ | \\n/ \")
erro6 = print ("  0  \n/ | \\n/ \")

'''


if __name__ == "__main__":
    joga_forca()

