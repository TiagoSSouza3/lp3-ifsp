def add_palavra(frase):
    dict = {}
    for palavra in frase:
        if palavra in dict:
            dict[palavra] += 1
        else:
            dict[palavra] = 1
    return dict

print("Contador de palavras")
frase = input("Digite uma crase para a contagem de palavras:\n")
frase = frase.split()
dict = add_palavra(frase)
print(dict)