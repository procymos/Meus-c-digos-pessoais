pe18 = homC = mu20 = 0
print(f"{'ANÁLISE DE DADOS':-^30}")
while True:
    idade = int(input('Informe sua idade:'))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = input('Informe seu sexo [M/F]:').strip().upper()[0]
    print(f'-'*30)
    if idade>18:
        pe18+=1
    if sexo in 'Mm':
        homC+=1
    if sexo in 'Ff' and idade<20:
        mu20+=1
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = input('Deseja continuar? [S/N]').strip().upper()[0]
    print(f'-' * 30)
    if continuar in 'Nn':
        break
print(f'\nA quantidade de pessoas com mais de 18 anos cadastradas foi: {pe18}\nA quantidade de homens cadastrados foi: {homC}\nA quantidade de mulheres com menos de 20 anos cadastradas foi: {mu20}')
