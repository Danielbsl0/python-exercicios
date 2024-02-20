letra = input('Insira uma letra: ').strip().upper()
if letra in 'AEIOU' and len(letra) == 1:
    print(f'{letra} é uma vogal.')
elif letra in 'BCDFGHJKLMNPQRSTVWXYZ' and len(letra) == 1:
    print(f'{letra} é uma consoante.')
else:
    print(f'{letra} é \033[31mINVÁLIDO\033[m')
