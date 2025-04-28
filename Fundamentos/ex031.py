dist = int(input('\033[1;34;40mQual distância da sua viagem em km? \033[m'))

if dist<=200:
    valor = dist*0.50
else:
    valor = dist*0.45

print(f'\033[1;30;43mSua viagem sairá no valor de: \033[m\033[1;30;47mR${valor:.2f}\033[m')