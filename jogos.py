import advinhacao
import forca

print("___________________")
print("Lista de jogos")
print("___________________")

print("1 - Advinhação")
print("2 - Forca")

jogo = int(input("Informe o jogo escolhido: "))

if jogo == 1:
    print("Jogo de advinhação")
    advinhacao.jogar_advinhacao()
else:
    print("Jogo da forca")
    forca.jogar_forca()
