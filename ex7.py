numero = 50;
qtNumero = media = soma = 0;
while numero <= 70: 
  if numero % 2 == 0:
    qtNumero = qtNumero + 1;
    soma = soma + numero;
  numero = numero +1;
media = soma/qtNumero;
print(f'média dos números pares = {media}');
