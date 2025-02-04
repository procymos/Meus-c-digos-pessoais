cont = soma = 0
while True:
    valor = int(input('Digite um valor inteiro [999 para parar]: '))
    if valor==999:
        break
    soma+=valor
    cont+=1
print(f'\nA soma do(s) {cont} valor(res) é igual a {soma}.')
