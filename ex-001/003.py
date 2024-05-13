#Faça um algoritmo para ler dois números e imprimir o maior, o menor ou então dizer se são iguais.
n1=float(input("Insira o primeiro numero:"))
n2=float(input("Insira o segundo numero:"))

if n1 > n2:
    print("O maior é:", n1, "O menor é:", n2)
else:
    if n2 > n1:
        print("O maior é:", n2, "O menor é", n1)
    else:
        print("Os dois são IGUAIS!")