dias=int(input('Quantos dias você usou o veículo ao total? '))
kmper=float(input('Quantos km você percorreu com o carro? km'))
preçodia=60.0*dias
preçokm=0.15*kmper

print(f'O total pelo aluguel do veículo é R${preçodia+preçokm:.2f}')
