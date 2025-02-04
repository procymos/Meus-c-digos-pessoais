va = 0
vb = 1
vg = 0
n = int(input('Informe a quantidade de termos da Sequência Fibonacci que deseja que sejam imprimidos:'))
print('\n', end='')
cont = 0
while cont != n:
    if cont == 0:
        print(f'{va} ⭢ ', end='')
    else:
        print(f'{vb} ⭢ ', end='')
        vg = vb
        vb = vb+va
        va = vg
    cont += 1
print('FIM!')
