
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

print(f"O resultado da divisão de {dividendo} por {divisor} é igual a {resultado} e tem resto igual a {resto}.")
