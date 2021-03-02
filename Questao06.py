
inicio = int(input("Informe o início da tabuada: "))
fim = int(input("Informe o fim agora: "))
while fim < inicio:
  fim = int(input("Informe o fim agora (tem que ser maior do que o início): "))

n = int(input("Tabuada de: "))
x = inicio
while x <= fim:
  print(f"{n} + {x} = {n + x}")
  x = x + 1
