from random import randint
ganhando = 'S'
cont = soma = maquina = valor = 0
while True:
    if ganhando not in 'Ss':
        break
    valor = int(input('Digite um valor de 1 a 10:'))
    selec = ' '
    while selec not in 'PI':
        selec= input('Par ou ímpar? [P/I]').strip().upper()[0]
    maquina = randint(0,10)
    soma = maquina+valor
    if (soma%2==0 and selec in 'Ii') or (soma%2!=0 and selec in 'Pp'):
        ganhando = 'F'
    else:
        print(f'\nVOCÊ GANHOU\n\nVocê jogou {valor} e a máquina jogou {maquina}. Total {soma}, deu ', end='')
        if soma%2==0:
            print('PAR!\n')
        else:
            print('ÍMPAR!\n')
        cont+=1
print(f'\nVOCÊ PERDEU APÓS GANHAR {cont} VEZES\n\nVocê jogou {valor} e a máquina jogou {maquina}. Total {soma}, deu ', end='')
if soma%2==0:
    print('PAR!\n')
else:
    print('ÍMPAR!\n')
