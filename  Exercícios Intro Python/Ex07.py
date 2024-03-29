def main():
    try:
        altura = float(input("Digite sua altura: "))
        peso = float(input("Digite seu peso: "))
    except:
        print("Valor invalido")
        return
    
    imc = peso / (altura * altura)

    def ver_imc():
        if imc < 18.5:
            return "Baixo peso"
        elif imc <= 24.5:
            return "Peso normal"
        elif imc <= 29.9:
            return "Excesso de peso"
        elif imc <= 34.9:
            return "Obesidade Grau 1"
        elif imc <= 39.9:
            return "Obesidade Grau 2"
        elif imc >= 40:
            return "Obesidade Grau 3"
        else:
            return "ERROR"

    print("Estado do peso atual: " + ver_imc())

    if ver_imc() != "Peso normal":
        peso_ideal = 24.9 * altura * altura
        peso = peso_ideal - peso

        if peso > 0:
            print("Você deve ganhar " + f'{peso:.2f}' + "Kg para entrar no peso ideal")
        else: 
            peso = peso * -1
            print("Você deve perder " + f'{peso:.2f}' + "Kg para entrar no peso ideal")

main()