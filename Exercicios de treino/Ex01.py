import random

def main():
    numero_correto = random.randint(0, 100)
    while numero_correto > 100 or numero_correto < 0:
        numero_correto = random.randint(0, 100)

    print("Numero sorteado!!! Tenta acertar o numero.")

    while True:
        numero_escolhido = input("Escolha um numero de 0 a 100: ")

        try:
            numero_escolhido = int(numero_escolhido)
            if numero_escolhido > 100 or numero_escolhido < 0:
                raise Exception
        except:
            print("Numero invalido")
            continue

        if numero_escolhido > numero_correto:
            print("O valor digitado é maior que o sorteado!")
        elif numero_escolhido < numero_correto:
            print("O valor digitado é menor que o sorteado!")
        else:
            print("Você encontrou, o numero sorteado era: " + str(numero_correto))
            jogar_denovo = input("Jogar denovo? S/N")
            if jogar_denovo == "S":
                main()
            return

main()