from string import ascii_letters

def main():
    print("COntador de vogais e consoantes")
    frase = input("Digite uma frase para contar o numero de consoantes e vogais nela:\n")

    vogais = "AaEeIiOoUu"
    consoantes = set(ascii_letters) - set(vogais)
    numero_de_vogais = 0
    numero_de_consoantes = 0

    for letra in frase:
        if letra in vogais:
            numero_de_vogais += 1
        elif letra in consoantes:
            numero_de_consoantes += 1

    print("O numero final foi:")
    print("Consoantes: " + str(numero_de_consoantes))
    print("Vogais: " + str(numero_de_vogais))

main()