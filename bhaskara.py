import math

while True:
    a = float(input("Informe a: "))
    b = float(input("Informe b: "))
    c = float(input("Informe c: "))

    delta = (b ** 2) - 4 * a * c

    if a == 0:
        print("O valor de a, deve ser diferente de 0")

    elif delta < 0:
        print("Sem raizes reais")

    else:
        x1 = (-b + math.sqrt(delta)) / 2 * a
        x2 = (-b - math.sqrt(delta)) / 2 * a
        print(f"O resultado é x1 = {x1} e x2 = {x2} ")

    opcao = input("Deseja continuar?(s/n): ")

    if opcao.lower() != "s":
        break
