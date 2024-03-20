def fazer_tabuada(numero):
    tabuada = []
    for multiplicador in range(1, 11):
        tabuada.append(numero * multiplicador)
    return tabuada

def main():
    print("VER TABUADA")
    try:
        numero = int(input("Digite o numero que vc quer saber a tabuada: "))
    except:
        print("numero invalido")
        return

    tabuada = fazer_tabuada(numero)

    for index, produto in enumerate(tabuada):
        print(str(numero) + " * " + str(index + 1) + ": " + str(produto))

main()