# Operadores
# aritméticos
# +*/-.

nota1 = 10
nota2 = 3
media = (nota1 + nota2) / 2

# potencia
numero = 2 ** 3 # elevado ao cubo
numero = 10 ** 2 # elevado ao quadrado


# lógicos
# and, or, not
# acesso liberado = nao bloqueado, idade > 18, horario comercial
bloqueado = False
idade = 21
horario = 10

horario_comercial = horario >= 8 and horario <= 18
maior_de_idade = idade > 18

if not bloqueado and maior_de_idade and horario_comercial:
    print("Liberado")
else:
    print("Não liberado")

# Operadores de comparação
# >, <, >=, <=, ==, !=
numeros = [1, 2, 3]
numeros2 = [1, 2, 3]

print(numeros == numeros2) #True

# Operados is
print(numeros is numeros2) #False

numeros3 = [1, 2]
numeros4 = numeros3
print(numeros3 is numeros4) #True
print(numeros3 is not numeros4) #False

# in (bool)
print("a" in "python")

prontuarios = ["SP001", "SP002", "SP003"]
prontuario = "SP001"
print(prontuario in prontuarios) #True

# sim, não, talvez
opcao = ""

if opcao == "sim" or opcao == "não" or opcao == "talvez":
    print("Opção Valida")
else: 
    print("Opcao Invalida")

opcoes = ("sim", "nao", "talve")

if opcao in opcoes:
    print("Opção Valida")
else:
    print("Opcão Invalida")