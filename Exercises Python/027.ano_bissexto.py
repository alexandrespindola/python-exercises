ano = int(input('Digite um ano: '))
if (ano%4==0 and  ano%100!=0) or (ano%400==0):
    print(f'{ano} é BISSEXTO')
else:
    print(f'{ano} NÃO é BISSEXTO')
