import random

palavra = ""
palavra_correta = ""
tentativas = 10

def verificar_letra(palavra, letra_usuario):
    palavra = palavra.split()
    for index, letra in enumerate(palavra_correta):
        if letra == letra_usuario:
            palavra[index] = letra
    
    return " ".join(palavra)

def gerar_palavra():
    palavras = ("python", "java", "formulario", "passado", "excel", "rapidamente", "aula", "lista", "tabela")
    return random.choice(palavras)

print("Jogo da forca")
print("Você pode errar até 10 vezes")
palavra_correta = gerar_palavra()
palavra = "_ " * len(palavra_correta)

while palavra.replace(" ", "") != palavra_correta:
    print(palavra)
    letra = input("Digite uma letra: ").lower()
    palavra_inicial = palavra
    palavra = verificar_letra(palavra, letra)
    if palavra == palavra_inicial:
        print("Não tem a letra '" + letra + "'")
        tentativas -= 1
        print("Numero de tentativas restantes: " + str(tentativas))
    if tentativas == 0:
        print("Acabaram as tentativas, você perdeu")
        print("A palavra era: " + palavra_correta)
        break

if palavra.replace(" ", "") == palavra_correta:
    print("Você venceu, a palavra era: " + palavra_correta)