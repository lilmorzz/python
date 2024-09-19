import random

def advinhar():

    # gerar numero

    numero_aleatorio = random.randint(1, 100)
    tentativas = 0


    while True:

        palpite = input("Digite um numero: ")

        if palpite == "sair":
            print("Voce saiu do jogo, o numero era: ", numero_aleatorio)
            break

        tentativas += 1
        palpite = int(palpite)

        if palpite > numero_aleatorio:
            print("Numero muito alto!")
        elif palpite < numero_aleatorio:
            print("Numero muito baixo!")
        else:
            print("Voce acertou! Tentativas: ", tentativas)
            break

advinhar()