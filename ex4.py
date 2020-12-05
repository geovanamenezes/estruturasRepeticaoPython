j = [];
c = [];
contador = 0;
encerrado = 0;
for i in range(0, 24):
    c.append(0);
    j.append(0);
print("Mapa de ocupação: (lugar - se ocupado)");
while contador != 48: 
  l = 0;
  while l < 24:
      print(f' {l+1}j-{j[l]} {l+1}c-{c[l]}    {l+2}c-{c[l+1]} {l+2}j-{j[l+1]}');
      l = l + 2; 
  print("escolha seu lugar:")
  opcao = input("J-Janela C-Corredor: ");
  numero = int(input("número do assento: "));
  if opcao == "J":
    if j[numero-1] == 0:
      print("VENDA EFETIVADA");
      j[numero-1] = 1;
    else:
      print("POLTRONA OCUPADA");
  elif opcao == "C":
    if c[numero-1] == 0:
      print("VENDA EFETIVADA");
      c[numero-1] = 1;
    else:
      print("POLTRONA OCUPADA");
  print("");
  contador = contador + 1;
print(" AGORA O ÔNIBUS ESTÁ LOTADO");