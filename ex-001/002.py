#Faça um algoritmo para ler três números e imprimir a soma, média e produto dos números lidos.
n1=float(input("Insira o primeiro numero:"))
n2=float(input("Insira o segundo numero:"))
n3=float(input("Insira o terceiro numero:")) #lê os numeros inseridos pelo usuário

soma=n1+n2+n3 #soma total
media=(n1+n2+n3)/3 # média dos numeros
produto = n1*n2*n3 # produto dos numeros

print(soma, media, produto)