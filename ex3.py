contador = 0;
numero1 = numero2 = numero3 = numero4 = numero5 = numero6 = 0;

while contador != 20: 
  numero = int(input("número do sorteado: "));
  if numero == 1:
    numero1 = numero1 + 1;
  elif numero == 2:
    numero2 = numero2 + 1;
  elif numero == 3:
    numero3 = numero3 + 1;
  elif numero == 4:
    numero4 = numero4 + 1;
  elif numero == 5:
    numero5 = numero5 + 1;
  elif numero == 6:
    numero6 = numero6 + 1;
  contador = contador + 1;

print(f' frequência dos números:');
print(f'1: {numero1}');
print(f'2: {numero2}');
print(f'3: {numero3}');
print(f'4: {numero4}');
print(f'6: {numero5}');
print(f'7: {numero6}');
