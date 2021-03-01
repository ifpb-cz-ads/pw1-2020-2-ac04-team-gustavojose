num = int(input("Informe um numero: "))
total = 0
cont = 0
while num > 0:
    total+=num
    cont+=1
    num = int(input("Informe 0 para sair ou continue informando outros numeros: "))

media = total/cont
print(f'{cont} numeros foram informados, e a soma foi {total}. A média aritmetica dos numeros informados é de {media:.2f}')