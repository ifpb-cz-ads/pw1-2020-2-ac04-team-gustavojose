
n = int(input("informe um número: "))

x = 3
if n > 2:
  while x < n:
    if n % 2 == 0 or n % x == 0:
      print(f"O número {n} não é primo.")
      break
    x += 2
  if x == n:
    print(f"o número {n} é primo.")
elif n == 2:
  print("O número 2 é primo.")
else:
  print(f"O número {n} não é primo.")
