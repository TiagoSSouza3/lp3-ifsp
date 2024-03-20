palavra = input("Digite uma palavra/frase: ")
print("Esta palavra é um palindromo") if palavra == palavra[::-1] else print("Esta palavra não é um palindromo")