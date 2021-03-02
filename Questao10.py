
pv = float(input("Informe o depósito inicial: "))
i = float(input("Informe a taxa de juros: "))
n = 12

fv = pv * pow((1 + i / 100), n)

print(f"O valor futuro é {fv:.2f}.")
