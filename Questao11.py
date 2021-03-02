deposito = float(input("Informe o seu deposito inicial: "))
juros = float(input("Informe a taxa de juros da poupança: "))
total_juros=0

for x in range(1,13):
    deposito+=deposito * juros/100
    total_juros+=deposito * juros/100
    print(f'Poupança no {x} mês = {deposito:.2f}')
    deposito_mensal = float(input("Informe o deposito deste mes: "))
    deposito+=deposito_mensal

print(f'O total de ganhos foi de: {total_juros:.2f}')