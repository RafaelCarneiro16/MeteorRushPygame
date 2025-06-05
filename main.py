from math import sqrt

x = int(input('Insira um numero: '))
if x > 10:
    print('O numero inserido é maior que 10')
elif x == 10:
    print('O numero inserido é igual que 10')    
else: 
    print('O numero inserido é menor que 10')

print(f'A raiz quadrada de {x} é {sqrt(x)}')
