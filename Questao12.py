
divida = float(input("Informe o valor da dívida: "))
juroMensal = float(input("Informe o valor do juro mensal: "))
parcela = float(input("Informe o valor a ser pago a cada mês: "))
meses = 0

while divida > 0:
  divida -= parcela
  divida += divida * juroMensal / 100
  meses += 1
  print(f"{divida:.2f}")

print(f"O valor de meses para quitar a dívida foi de {meses}.")
