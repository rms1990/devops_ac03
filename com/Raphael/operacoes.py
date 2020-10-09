def armstrong(n):
  soma = 0  
  temp = n  
  while temp > 0:  
    digito = temp % 10  
    soma += digito ** 3  
    temp //= 10  
  return n == soma
