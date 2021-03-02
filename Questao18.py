
dividendo = int(input("Informe o primeiro número: "))
divisor = int(input("Informe o segundo número: "))
soma = 0
resultado = 0
resto = 0

while soma <= dividendo:
  resto = dividendo - soma
  soma += divisor
  if resto != dividendo:
    resultado += 1

print(f"A divisão de {dividendo} por {divisor} tem resto igual a {resto}.")
