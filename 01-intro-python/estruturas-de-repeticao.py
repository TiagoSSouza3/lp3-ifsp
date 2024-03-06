# for, while (break/continue)

# for
for letra in "Hello World":
    print(letra)

numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)


# range
# range(5) = 0, 1, 2, 3, 4
# range(start=0, stop, step=1)
# range(0, 12, 2) # 0, 2, 4, 6, 8, 10
for i in range(5):
    print(i)


# 0 ate 100
list = list(range(101))
print(list)


# while
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# break
comando = ""
while True:
    comando = input("Digite o comando: ")
    if comando == "sair":
        break
    if comando == "1":
        print("1")

# continue
numeros = [-10, 3, 0, 5, 2, -2]

for numero in numeros:
    if numero <= 0:
        continue
    print(numero)
 
for numero in numeros:
    if numero > 0:
        print(numero)

# compreensão de listas
numeros = [1, 2, 3, 4, 5]
quadrados = []

for numero in numeros:
    quadrados.append(numero**2)

# [expressão for item in lista]
quadrados = [numero ** 2 for numero in numeros]

# [expressão for item in lista if condicao]
numeros = [-3 , 0, -5, 1, 2, 4]
poitivos = [numero for numero in numeros if numero > 0]
