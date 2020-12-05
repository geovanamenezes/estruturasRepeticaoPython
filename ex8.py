numero = 1;
contador = maior = menor = 0;
while numero >= 0:   
  numero = int(input("número:"));
  if numero >= 0:
    if contador == 0:
      maior = numero;
      menor = numero;
    if numero > maior:
      maior = numero;
    if numero < menor:
      menor = numero;
  contador = contador + 1;

print(f'maior número = {maior}');
print(f'menor número = {menor}');
