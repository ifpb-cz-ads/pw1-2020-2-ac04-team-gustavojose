
inicio = int(input("Informe o inicio da tabuada: "))
fim = int(input("Informe o fim agora: "))
while fim < inicio:
  fim = int(input("Informe o fim agora (tem que ser maior do que o inicio): "))

n = int(input("Tabuada de: "))
x = inicio
while x <= fim:
  print(f"{n} + {x} = {n + x}")
  x = x + 1
