# Tipo de dados

# Númerico

# int
idade = 10

# float
altura = 1.65

# Booleano
# True, False
verdade = True
mentira = False
ligado = True
frete_gratis = False

# str = string
# sequencia de caracteres
# literal de string em python
nome = "josé"
nome = 'josé'

# char
letra = "a"

frase = """
Ola Pessoal
Teste
Teste
"""

# Interpolação de string
nome = "Sonia"
idade = 23

# f - string
mensagem = f"Bom dia {nome}, Você tem {idade} anos!"

nome = "Silvio Santos"
print(nome [2])
print(nome [-5])
print(nome [0:4])

# str são objetos
# métodos
print(nome.upper())
print(nome)

# list
# lista de valores
# podem conter valores de tipos diferentes
# podem ser alterada (adicionar, remover)
habilidades = ["java", "html", "css"]
print(habilidades[0])

habilidades[0] = "javascript"
print(habilidades)

habilidades.append("python")
print(habilidades)

# adicionar em uma posição
habilidades.insert(0, "kotlin")
print(habilidades)

# remove, sort, clear, copy ...

for habilidade in habilidades:
    print(habilidade)

# tuple
# lista de valores
# não pode alterar os valores
opcoes = ("sim", "não", "talvez")
racas_rpg = ("anao", "humano", "elfo")

print(opcoes[1])

# função que retorna estatisticas
# sobre as notas de um aluno/aluna
# media, menor nota, maior nota
# entrada: n1, n2, n3 ou notas(list)
# saida: media, menor nota, maior nota
def estatistica_nota(notas):
    media = sum(notas)/len(notas)
    menor = min(notas)
    maior = max(notas)
    return media, menor, maior

notas = [4, 7, 10]
estatisticas = estatistica_nota(notas)
print(estatisticas)
print(type(estatisticas))

# desempacotamento de tuple
media, menor, maior = estatisticas
print(media, menor, maior)

# set
# conjunto de valores
# não permite valores duplicados
# não é indexado
habilidades = {"java", "python", "css"}
habilidades.add("java")
print(habilidades)

# dict
# dicionario
# palavra
# palavra => definição
# chave => valor
# key => value
nome = "Silvio Santos"
casado = True
idade= 120

pessoa = {
    "nome": "Silvio Santos",
    "casado": True,
    "idade": 120
}

print(pessoa["casado"])
print(pessoa["idade"])
print(pessoa["nome"])

pessoa["rico"] = True
print(pessoa)

# none
# null
nulo = None
