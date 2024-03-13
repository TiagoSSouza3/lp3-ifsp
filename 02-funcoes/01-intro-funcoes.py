# Funçoes
# Modularizar o programa
# Reuso
# Manutenabilidade (correção de erros e novas funcionalidades)

# Declaração
def ola_mundo():
    print("Olá Mundo")

# Chamada
ola_mundo()
ola_mundo()

# Função sem retorno
# Side effect - Efeito Colateral
def imprimir_mensagem(nome):
    print(F"Bom dia, {nome}")

imprimir_mensagem("TR3S")

# Função com retorno
# Funçãp pura
def mensagem(nome):
    return f"Bom dia , {nome}"

print(mensagem("Tirigo"))

# Parâmetros e Argumentos
def somar(n1, n2):
    return n1 + n2

numero = 4
print(str(somar(9, numero)))
print(str(somar(9, 4)))
print(str(somar(9, somar(1, 3))))

# Escopo de variaveis
def media(nota1, nota2, nota3):
    total = nota1 + nota2 + nota3
    return total / 3

print(media(13, 14, 12))

# Parâmetros com valor padrão
def mensagem(nome, mensagem="bom dia"):
    return f"{mensagem}, {nome}"

print(mensagem("luffy"))

# Argumentos Nomeados
print("ola", "123", "teste", sep = "<>", end = "\n\n")
print("TESTE")

print(mensagem(nome = "Lucas", mensagem = "Boa Tarde "))
print(mensagem(mensagem = "Boa Tarde ", nome = "Lucas"))

# docstring
# comentario de documentação
def somar(n1, n2):
    '''
    Função que soma dois números
    :param n1: primeiro número
    :param n2: segundo número
    '''
    return n1 + n2

somar(2, 5)

# FUnções built-in
# print, type, len, sum, max, min, input
# ver python3 interativo terminal

def media(*notas):
    return sum(notas) / len(notas)

print(media(10, 30, 20, 4, 9, 29))