def fatorial_iterativo(n):
  f = 1
  for i in range(1, n+1):
    f = f*i
  return f

numero = int(input('informe o valor: \n'))
print(f'O FATORIAL DE {numero} é: {fatorial_iterativo(numero)}')
