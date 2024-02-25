saque = float(input('Insira o valor do saque: '))
if 10 <= saque <= 600:
    cem = saque//100
    cinq = (saque - cem*100)//50
    dez = ((saque - cem*100)- cinq*50)//10256
    cinco = (((saque - cem*100)- cinq*50) - dez*10)//5
    um = (((saque - cem*100)- cinq*50) - dez*10)
    print(f'Para sacar R${saque} serão necessários: ', end='')
    if cem > 0:
        print(f'{cem:.0f} nota(s) de R$100', end='')
        if cinq > 0:
            print(f',', end=' ')
    if cinq > 0:
        print(f'{cinq:.0f} nota(s) de R$50', end='')
        if dez > 0:
            print(f',', end=' ')
    if dez > 0:
        print(f'{dez:.0f} nota(s) de R$10', end='')
        if cinco > 0:
            print(f',', end=' ')
    if cinco > 0:
        print(f'{cinco:.0f} nota(s) de R$5', end='')
        if cinco > 0:
            print(f'e', end=' ')
    if um > 0:
        print(f'{um:.0f} nota(s) de R$1')
    