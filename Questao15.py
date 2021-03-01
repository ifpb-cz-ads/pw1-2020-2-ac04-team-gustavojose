num = 0
def tabuada(num):
    if operacao == 'S':
        print('Saiu com sucesso!')
    else:
        num = int(input('Informe um numero: '))
        y = 11
        if operacao == '*':
            for y in range(1, y):
                print(f'{num}*{y} = {num*y}')
        elif operacao == '/':
            for y in range(1, y):
                print(f'{num*y}/{y} = {num*y/num}')
        elif operacao == '+':
            for y in range(1, y):
                print(f'{num}+{y} = {num+y}')
        elif operacao == '-':
            for y in range(1, y):
                print(f'{num}-{y} = {num-y}')
        else:
            print('Operacao invalida')
        

print('''
[+] - para adição
[-] - para subtração
[/] - para divisão
[*] - para multiplicação
[S] - para sair''')

operacao = input('Informe uma opção: ')
tabuada(num)

while operacao != 'S':
    print('''
    [+] - para adição
    [-] - para subtração
    [/] - para divisão
    [*] - para multiplicação
    [S] - para sair''')

    operacao = input('Informe uma opção: ')
    tabuada(num)
