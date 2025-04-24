num = int(input('Informe um número: '))
unidade = num//1 % 10
dezena = num//10 % 10
centena = num//100 % 10
milhar = num//1000 % 10
print(f'Analisando o número {num}:')

print(f'Unidade: {unidade}\n'
      f'Dezena: {dezena}\n'
      f'Centena: {centena}\n'
      f'Milhar: {milhar}\n')
