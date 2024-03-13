def main():
    numero = input("Digite um numero inteiro: ")

    try:
        numero = int(numero)
    except:
        print("Isso não é um numero inteiro")
        return
        

    def sucessor(numero: int) -> int:
        return numero + 1

    def antecessor(numero: int) -> int:
        return numero - 1

    print("Sucessor: " + str(sucessor(numero)))
    print("Antecessor: " + str(antecessor(numero)))

main()