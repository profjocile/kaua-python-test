n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))

if n1 % n2 == 0: # Se n1 é divisível por n2
    print(f"{n1} é", end=' ')
else:
    print(f"{n1} não é ", end=' ')

print(f"divisível por {n2}")