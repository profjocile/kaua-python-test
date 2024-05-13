n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))

# Verificando se n2 é diferente de zero para evitar divisão por zero
if n2 != 0:
    # Verificando se o resto da divisão é zero
    if n1 % n2 == 0:
        # Verificando se n1 é divisível por 2 para determinar se é inteiro
        if n1 % 2 == 0:
            print(f"{n1} é um número inteiro divisível por {n2}")
        else:
            print(f"{n1} é um número não inteiro divisível por {n2}")
    else:
        print(f"{n1} não é divisível por {n2}")
else:
    print("Erro: Divisão por zero.")
