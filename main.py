vendatotal = float(input('digite valor total:'))
boletos = float(input('digite valor dos boletos: '))
salarios = float(input('digite valor dos salarios: '))
gastosloja = float(input('digite valor dos gastos: '))
aluguel = float(input('digite o valor so aluguel: '))

soma = vendatotal - (boletos + salarios + gastosloja + aluguel)

porcentagem_boletos = (boletos / vendatotal) * 100
porcentagem_salarios = (salarios / vendatotal) * 100
porcentagem_gastosloja = (gastosloja / vendatotal) * 100
porcentagem_aluguel = (aluguel / vendatotal) * 100

print('O valor de fechamento de caixa é de {}.'.format(s))
print(f'O valor dos boletos equivale a {porcentagem_boletos :.2f}% do valor total das vendas')
print(f'O valor dos salarios equivale a {porcentagem_salarios :.2f}% do valor total das vendas')
print(f'O valor dos gastos da loja equivalem a {porcentagem_gastosloja :.2f} do valor total das vendas')
print(f'O valor do aluguel equivale a {porcentagem_aluguel :.2f}% do valor total das vendas')
