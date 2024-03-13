def main():
    prontuario = input("Digite o prontuario: ")

    if validador(prontuario):
        print("Funcionario Existente")
    else:
        print("Funcionario Invalido")

    def validador(prontuario: str):
        validador = len(prontuario) == 7 and prontuario[0:2] == "BR" and int(prontuario[2:6]) >= 1 and int(prontuario[2:6]) <= 9999 and prontuario[6] == "X"
        return validador


main()