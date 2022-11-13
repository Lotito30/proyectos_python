import random
from words import words
import string


def buscar_palabra(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    vidas = 5
    palabra_adivinar = buscar_palabra(words)
    letra_adivinar = set(palabra_adivinar)
    abecedario = set(string.ascii_uppercase)
    if len(palabra_adivinar) >= 5:
        pista = random.choices(palabra_adivinar, k=2)
    else:
        pista = random.choice(palabra_adivinar)
    letras_array = set(pista)

    while len(letra_adivinar) > 0 and vidas > 0:

        print("Letras usadas:",''.join(i for i in sorted(letras_array)))
        print('____________________________')
        print('Descubre la palabra:',''.join(i if i in letras_array else '_' for i in palabra_adivinar))
        print('____________________________')
        letra_ingresada = input('Letra: ').upper()
        print('____________________________')
        if letra_ingresada not in abecedario:
            print(f'{letra_ingresada} no es valido. Ingrese una letra.')
            print('____________________________')
        else:
            letras_array.add(letra_ingresada)
            if letra_ingresada in letra_adivinar:
                letra_adivinar.remove(letra_ingresada)
        vidas -= 1

    if vidas > 0 or len(palabra_adivinar) == 0:
        print('Felicidades.')
    else:
        print('Game Over')

if __name__ == '__main__':
    hangman()
