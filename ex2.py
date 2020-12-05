qtQuilowatts = 1;
acrescimo = 0;
faturamento = 0;
qtdConsumidores = 0;


salarioMinimo = float(input("Salário Mínimo: "));
while qtQuilowatts != 0: 
  qtQuilowatts = float(input("Quantidade Quilowatts: "));
  if qtQuilowatts != 0:    
    print("Tipo de consumidor: ");
    print(" 1 - residencial");
    print(" 2 - comercial");
    tipo = int(input(" 3 - residencial:   "));
    valorQuilowatts = salarioMinimo/8;
    valorGasto = qtQuilowatts * valorQuilowatts;
    if tipo == 1:
      acrescimo = valorGasto * 0.05
    if tipo == 2:
      acrescimo = valorGasto * 0.1
    if tipo == 3:
      acrescimo = valorGasto * 0.15
    valorAPagar = valorGasto + acrescimo;
    faturamento = faturamento + valorAPagar;
    if valorAPagar >= 500 and valorAPagar <= 1000:
      qtdConsumidores = qtdConsumidores + 1;
    print(f'valor de cada Quilowatts: {valorQuilowatts}');
    print(f'valor a ser pago por esse consumidor: {valorAPagar}');

print(f'faturamento geral da empresa {faturamento}');
print(f'quantidade de consumidores que pagam entre 500,00 e 1000,00: {qtdConsumidores}');
