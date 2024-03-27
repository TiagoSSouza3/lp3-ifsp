nota = float(input("Digite a nota numerica: "))
if nota == 10:
    print("nota: A")
elif nota < 10 and nota >= 7.5:
    print("nota: B")
elif nota < 7.5 and nota >= 5:
    print("nota: C")
elif nota < 5 and nota >= 2.5:
    print("nota: D")
elif nota < 2.5 and nota >= 0:
    print("nota: E")
else:
    print("NOta invalida")