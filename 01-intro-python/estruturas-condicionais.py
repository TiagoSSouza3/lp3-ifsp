# if, if/else, if/elif/else, ternario, match

# if
# if condition:
#    codigo do if
#    codigo do if
#
# codigo

idade = 20

if idade >= 18:
    print("Maior de Idade")

print("Fora do if")


# if/else
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

# elif
# criança 0 12, adolecente 12 17, adulto 18 59, idoso 60+

if idade <= 12:
    print("criança")
elif idade <= 17:
    print("adolecente")
elif idade <= 59:
    print("adulto")
else:
    print("idoso")

# evitar aninhamento de if

email = ""
senha = ""

if email == "admin@gmail.com":
    if senha == "123admin":
        print("liberado")
    else:
        print("senha ou email invalidos")
else:
        print("senha ou email invalidos")

if email == "admin@gmail.com" and senha == "123admin":
    print("liberado")
else:
    print("senha ou email invalidos")

# entrada numero 1, 2, 3, 4 ... 7
# saida dia: Domingo, Segunda ... Sabado

dia = 4

dias = {
    1: "Domingo",
    2: "Segunda",
    3: "Terça",
    4: "Quarta",
    5: "Quinta",
    6: "Sexta",
    7: "Sabado"
}

if dia in dias:
    print(dias[dia])
else:
    print("Dia invalido")

# ternario
media = 8.0

if media >= 6.0:
    situacao = "aprovado"
else:
    situacao = "reprovado"

situacao = "aprovado" if media >= 6 else "reprovado"

# match

match dia:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5:
        print("Quinta")
    case 6:
        print("Sexta")
    case 7:
        print("Sabado")
    case _:
        print("invalido")

# dia util 2, 3, 4, 5, 6
# fim de semana 1, 7

match dia:
    case 1 | 7:
        print("Fim de semana")
    case 2 | 3 | 4 | 5 | 6:
        print("Dia util")
    case _:
        print("Invalido")