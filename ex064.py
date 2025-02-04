valor = 0
cont = 0
soma = 0
while valor != 999:
    valor = int(input('Digite um valor inteiro qualquer (999):'))
    if valor != 999:
        soma+=valor
        cont+=1
print(f'\nA soma do(s) {cont} valor(es) digitados é {soma}.')
