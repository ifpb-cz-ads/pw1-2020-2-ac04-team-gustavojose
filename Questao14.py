
compras = []
while True:
  preco = 0.0
  codigo = int(input("Informe o código do produto: "))
  if codigo == 0:
    break
  quantidade = int(input("Informe a quantidade comprada: "))

  if codigo == 1:
    preco = 0.5
  elif codigo == 2:
    preco = 1
  elif codigo == 3:
    preco = 4
  elif codigo == 5:
    preco = 7
  elif codigo == 9:
    preco = 8
  else:
    print("Código inválido")
  
  if quantidade <= 0:
    print("Quantidade inválida")

  if preco != 0 and quantidade > 0:
    compras.append([codigo, quantidade, preco])

soma = 0.0
for p in compras:
  print(f"{p[0]} x {p[1]} por {p[2]:.2f}: {p[1] * p[2]:.2f}")
  soma += p[1] * p[2]
print(f"Total: {soma:.2f}")
