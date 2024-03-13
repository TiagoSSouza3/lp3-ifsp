def main():
    try:
        numero1 = float(input("Digite o primeiro numero: "))
        numero2 = float(input("Digite o segundo numero: "))
        numero3 = float(input("Digite o terceiro numero: "))
    except:
        print("Numero invalido")
        return

    def media(*numeros):
        return sum(numeros) / len(numeros)

    print("Media: " + str(media(numero1, numero2, numero3)))

main()