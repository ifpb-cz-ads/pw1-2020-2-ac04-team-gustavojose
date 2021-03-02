lista = [9,7,2,4]
menor = lista[0]
for elemento in lista:
	if elemento < menor:
    		menor = elemento
print(f'O menor numero da lista é {menor}')
