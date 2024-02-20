n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
if n1 > n2:
    print(f'O maior valor entre os dois é: {n1}')
elif n2 > n1:
    print(f'O maior valor entre os dois é: {n2}')
else:
    print(f'Os valores inseridos são iguais.')
