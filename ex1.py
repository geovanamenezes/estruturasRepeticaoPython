idade = 1;
qtdeSexoFeminino = 0;
mulheres21 = 0;
menorIdade = 100;
qtdeSexoMasculino = 0;
somaIdadeMasculino = 0;
masculinosMaiores45 = 0;
qtdeComExperiencia = 0;
while idade != 0:
  idade = int(input("Idade (digite 0 para finalizar): "));
  if idade != 0:
    sexo = str(input("Sexo: "));
    experiencia = str(input("Tem expriência? S-Sim N-Não: "));
    if sexo == "F":
      qtdeSexoFeminino = qtdeSexoFeminino + 1;
      if experiencia =="S":
        if idade < 21:
          mulheres21 = mulheres21 + 1;
        if idade < menorIdade:
          menorIdade = idade;
    elif sexo == "M":
      qtdeSexoMasculino = qtdeSexoMasculino +1;
      if experiencia == "S":
        qtdeComExperiencia = qtdeComExperiencia + 1;
        somaIdadeMasculino = somaIdadeMasculino + idade;
      if idade > 45:
        masculinosMaiores45 = masculinosMaiores45+1;

print(f' Número de candidatos do sexo feminino: {qtdeSexoFeminino}');
print(f'Número de candidatos do sexo masculino: {qtdeSexoMasculino}');
print(f'Idade média dos homens que tem experiência: {somaIdadeMasculino/qtdeComExperiencia}');
print(f'A porcentagem dos homens com mais de 45 anos entre o total dos homens: {masculinosMaiores45*100/qtdeSexoMasculino} % '); 
print(f'O número de mulheres com idade inferior a 21 anos e com experiência no serviço: {mulheres21} ');    
print(f'A menor idade entre as mulheres que já tem experiência no serviço.: {menorIdade} ');