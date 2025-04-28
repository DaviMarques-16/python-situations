velocidade=float(input('Qual velocidade do carro? '))

if velocidade>80:
    multa = (velocidade-80)*7
    print(f'Acima da velocidade permitida! Deverá pagar a multa de : R${multa:.2f}')
else:
    print('Parabéns! Você é um motorista responsável.')
