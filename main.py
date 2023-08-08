# Solicita ao usuário os valores relacionados às finanças da loja
vendatotal = float(input('Digite o valor total das vendas: '))
boletos = float(input('Digite o valor dos boletos: '))
salarios = float(input('Digite o valor dos salários: '))
gastosloja = float(input('Digite o valor dos gastos da loja: '))
aluguel = float(input('Digite o valor do aluguel: '))

# Calcula a soma do saldo disponível após dedução dos gastos
soma = vendatotal - (boletos + salarios + gastosloja + aluguel)

# Calcula as porcentagens de cada gasto em relação ao valor total das vendas
porcentagem_boletos = (boletos / vendatotal) * 100
porcentagem_salarios = (salarios / vendatotal) * 100
porcentagem_gastosloja = (gastosloja / vendatotal) * 100
porcentagem_aluguel = (aluguel / vendatotal) * 100

# Exibe o valor de fechamento de caixa após dedução dos gastos
print('O valor de fechamento de caixa é de {}.'.format(soma))

# Exibe as porcentagens dos gastos em relação ao valor total das vendas
print(f'O valor dos boletos equivale a {porcentagem_boletos:.2f}% do valor total das vendas')
print(f'O valor dos salários equivale a {porcentagem_salarios:.2f}% do valor total das vendas')
print(f'O valor dos gastos da loja equivale a {porcentagem_gastosloja:.2f}% do valor total das vendas')
print(f'O valor do aluguel equivale a {porcentagem_aluguel:.2f}% do valor total das vendas')
