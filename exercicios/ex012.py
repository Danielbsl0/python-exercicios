valor = float(input('Insira o valor da hora: R$'))
h = int(input('Insira a quantidade de hora: '))
salb = h*valor
if salb <= 900:
    ir = 0
    perc = 0
elif salb <= 1500:
    ir = salb*5/100
    perc = 5
elif salb <= 2500:
    ir = salb*10/100
    perc = 10
else:
    ir = salb*20/100
    perc = 20
sall = salb-(ir+salb*10/100)
print(f'Salário Bruto: R${salb}\n(-) IR ({perc}%): R${ir}\n(-) INSS (10%): R${salb*10/100}\nFGTS(11%): R${salb*11/100}\nTotal de descontos: R${ir+salb*10/100}\nSalário Líquido: {sall}')

