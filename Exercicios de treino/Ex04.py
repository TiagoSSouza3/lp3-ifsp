import random

def criar_candidatos():
    first_names=("Tharik", "Raul", "Mateus", "Leticia", "Rodrigo", "Paulo")
    last_names=("Ramos", "Santos", "Guimarães", "Silva", "Souza", "Brasão")

    candidatos = []
    for x in range(3):
        candidatos.append(random.choice(first_names) + " " + random.choice(last_names))

    return candidatos

def main():
    candidatos = criar_candidatos()
    votos = [0, 0, 0]

    print("Votação, vote quantas vezes quiser nos candidatos a seguir de acordo com o numero:")
    for index, candidato in enumerate(candidatos):
        print(candidato + "(" + str(index + 1) + ");")

    while True:
        voto = input("Digite o numero do candidato que deseja votar: ")
        match voto:
            case "1":
                votos[0] += 1
            case "2":
                votos[1] += 1
            case "3":
                votos[2] += 1
            case _:
                print("Voto invalido")

        escolha = input("Deseja votar novamente? S/N: ")
        if escolha != "S":
            break

    print("Resultados Finais:")
    for index, candidato in enumerate(candidatos):
        print(candidato + ": " + str(votos[index]) + "\n")
    
    if max(votos) == min(votos):
        print("Todos empataram com " + str(max(votos)) + "votos cada")
    elif votos[0] == votos[1] and votos[0] ==  max(votos):
        print("Os candidatos: " + candidatos[0] + " e " + candidatos[1] + " empataram com " + str(max(votos)) + "votos cada")
    elif votos[1] == votos[2] and votos[1] ==  max(votos):
        print("Os candidatos: " + candidatos[1] + " e " + candidatos[2] + " empataram com " + str(max(votos)) + "votos cada")
    elif votos[0] == votos[2] and votos[2] ==  max(votos):
        print("Os candidatos: " + candidatos[0] + " e " + candidatos[2] + " empataram com " + str(max(votos)) + "votos cada")
    else:
        for index, numero_votos in enumerate(votos):
            if numero_votos == max(votos):
                print("O grande vencedor foi o candidato " + candidatos[index] + " com " + str(max(votos)) + " votos")




main()