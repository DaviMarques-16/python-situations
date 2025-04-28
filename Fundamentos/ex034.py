salário=float(input('Qual salário do funcionário? R$'))

if salário>1250:
    aumento = salário*0.1
    novo = salário+(aumento)
    print(f'Seu salário recebeu aumento de R${aumento:.2f} e passa a ser R${novo:.2f} ')
else:
    aumento = salário*0.15
    novo = salário+(salário*0.15)
    print(f'Seu salário recebeu aumento de R${aumento:.2f} e passa a ser R${novo:.2f}')
print('\033[1;38;40mObrigado por se esforçar pela empresa!\033[m')
