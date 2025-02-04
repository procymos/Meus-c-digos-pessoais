media = 0
cd = 0
cn = 'S'
maior = 0
menor = 0
while cn in 'Ss':
    valor = int(input('Digite um valor inteiro:'))
    if valor > maior:
        maior= valor
    if valor<menor or cd==0:
        menor = valor
    cd+=1
    media+=valor
    cn = input('Deseja continuar? [S/N]\n').strip().upper()[0]
media= media/cd
print(f'\nLoop finalizado.\n\nA media do(s) {cd} valor(es) é igual a {media:.2f}\nO maior valor foi {maior} e o menor valor foi {menor}.')
