
deposito = float(input("Informe o seu depósito inicial: "))
juros = float(input("Informe a taxa de juros da poupança: "))
totalJuros = 0

for x in range(1, 13):
  deposito += deposito * juros / 100
  totalJuros += deposito * juros / 100
  print(f"Poupança no {x} mês = {deposito:.2f}")

print(f"O total de ganhos foi de: {totalJuros:.2f}.")
