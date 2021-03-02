
maximo = 10
contagem = maximo

while True:
  print(f"{contagem}")
  if contagem == 0:
    print("Fogo!")
    break
  contagem -= 1
