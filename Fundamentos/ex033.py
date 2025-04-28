n1=float(input('\033[1;30;47mDigite um valor: \033[m'))
n2=float(input('\033[1;30;47mDigite o segundo valor: \033[m'))
n3=float(input('\033[1;30;47mDigite o terceiro e último valor: \033[m'))

sort = [n1,n2,n3]
print(f'\033[1;31;40mO maior número é {max(sorted(sort))}\033[m\n'
      f'\033[1;31;40mO menor número é {min(sorted(sort))}\033[m')
