qtd_primos = int(input('Informe a quantidade de numeros primos que deseja imprimir: '))
qtd=0
n=0
aux=0
cont=0

while qtd <= qtd_primos:
    n+=1
    cont=0

    for aux in range(1,n+1):
        if n % aux == 0:
            cont+=1
        aux+=1

    if cont == 2:
        print(n)
        qtd+=1