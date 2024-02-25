sal = float(input('Insira o seu salário atual: R$'))
if sal <= 280:
    sal2 = sal + sal*20/100
    perc = 20
elif sal < 700:
    sal2 = sal + sal*15/100
    perc = 15
elif sal < 1500:
    sal2 = sal + sal*10/100
    perc = 10
else:
    sal2 = sal + sal*5/100
    perc = 5
print(f'O seu salário antes do reajuste era de: R${sal}\nO percentual aplicado foi de {perc}%\nO valor do aumento foi de {sal2-sal}\nO seu novo salário é: R${sal2}')
