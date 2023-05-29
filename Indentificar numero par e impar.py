def primo(n):
  if(n<2):
    return False
  i = n//2
  while(i>1):
    if(n%i==0):
      return False
    i = i-i
  return True
    
def imprimir_resultado(numero, resultado):
  mensagem = (f'O número {numero} é PAR')
  if(resultado):
    mensagem = (f'O número {numero} é IMPAR')
  return mensagem
    
    
numero = int(input('Informe o numero: \n'))
resultado = primo(numero)
msg = imprimir_resultado(numero, resultado)
print(msg)