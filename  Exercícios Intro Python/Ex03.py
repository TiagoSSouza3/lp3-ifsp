def main():
    try:
        valor = float(input("Digite o valor da compra: "))
    except:
        print("Valor invalido")
        return

    def mensagem(valor):
        return f"Valor Final: {valor}"

    if valor >= 0.01 and valor <= 9.99:
        print(mensagem(valor))
    elif valor >= 10.00 and valor <= 99.99:
        valor -= valor * 5/100
        print(mensagem(valor))
    elif valor >= 100.00 and valor <= 499.99:
        valor -= valor * 10/100
        print(mensagem(valor))
    elif valor >= 500.00:
        valor -= valor * 15/100
        print(mensagem(valor))
    else:
        print("Valor invalido")

main()