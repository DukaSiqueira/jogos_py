import random


def jogar_advinhacao():
    print("___________________")
    print("Bem-vindo ao jogo de advinhação")
    print("___________________")

    numero_secreto = random.randrange(1, 101)
    acertou = False
    total_tentativas = 0
    pontos = 1000

    print("Niveis de dificuldade")
    print("1 - Fácil", "2 - Médio", "3 - Difícil", sep="\n")
    nivel = int(input("Informe o nível de dificulade desejado:"))

    if nivel == 1:
        total_tentativas = 20
    elif nivel == 2:
        total_tentativas = 10
    elif nivel == 3:
        total_tentativas = 5
    else:
        print("Informe um nível válido")

    for rodada in range(1, total_tentativas + 1):

        print("Tentativa {} de {}".format(rodada, total_tentativas))
        tentativa = int(input("Digite um número entre 1 e 100:"))

        if tentativa < 1 or tentativa > 100:
            print("Digite um número válido, entre 1 e 100")
            continue

        acertou = tentativa == numero_secreto
        maior = tentativa < numero_secreto
        menor = tentativa > numero_secreto

        if acertou:
            print("Você acertou e fez {} pontos".format(pontos))
            break
        else:
            if maior:
                print("Você errou! O número secreto é maior.")
            elif menor:
                print("Você errou! O número secreto é menor.")
            pontos_perdidos = abs(numero_secreto - tentativa)
            pontos = pontos - pontos_perdidos

    print("O número era {}!".format(numero_secreto))
    print("O jogo terminou!")


if __name__ == "__main__":
    jogar_advinhacao()
