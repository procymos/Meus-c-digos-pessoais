print(f"{'TABUÁDA LOMBRADA':*^40}")
while True:
    num = int(input('Digie um valor:'))
    if num<0:
        break
    print('-'*30, '\n',end='')
    for c in range(1,11):
        print(f"""
        {num} x {c} = {num*c}""")
    print('\n', end='')
    print('-'*30)
print('-'*30,'\n\nPROGRAMA FINALIZADO!')