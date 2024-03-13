def main():
    try:
        comprimento = float(input("Digite o comprimento do aquario: "))
        altura = float(input("Digite o altura do aquario: "))
        largura = float(input("Digite o largura do aquario: "))
        temperatura_desejada = float(input("Qual a temperatura desejada para o aquario: "))
        temperatura_ambiente = float(input("Qual a temperatura ambiente do local do aquario: "))
    except:
        print("Valor invalido")
        return

    dimensoes = [comprimento, largura, altura]

    def volume(dimensoes):
        return (dimensoes[0] * dimensoes[1] * dimensoes[2]) / 1000
    
    def filtragem_minima():
        return volume(dimensoes) * 2
    
    def filtragem_maxima():
        return volume(dimensoes) * 3
    
    def potencia():
        return volume(dimensoes) * 0.05 * (temperatura_desejada - temperatura_ambiente)

    print("Volume do aquario: " + str(volume(dimensoes)))
    print("Filtragem minima: " + str(filtragem_minima()))
    print("Filtragem maxima: " + str(filtragem_maxima()))
    print("Temperatura ideal do termostato: " + str(potencia()))

main()