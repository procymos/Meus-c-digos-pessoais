print(f"{'BANCO DO PRO':=^30}")
c50 = c20 = c10 = c1 = 0
while True:
    valor = int(input('Informe o valor que deseja sacar: R$'))
    if valor >=50:
        while valor >=50:
            valor -= 50
            c50 += 1
        print(f'Total de {c50} cédulas de R$50')
    if valor >=20:
        while valor >=20:
            valor -=20
            c20+=1
        print(f'Total de {c20} cédulas de R$20')
    if valor >=10:
        while valor>=10:
            valor-=10
            c10+=1
        print(f'Total de {c10} cédulas de R$10')
    if valor>=1:
        while valor>=1:
            valor-=1
            c1+=1
        print(f'Total de {c1} moedas de R$1')
    if valor==0:
        break
