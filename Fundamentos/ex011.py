largura=float(input('Qual largura da sua parede em metros? '))
altura=float(input('Qual altura da sua parede em metros? '))
area=largura*altura
litro=2

print(f'A dimensão da parede é {largura:.2f}x{altura:.2f} e sua área é: {area:.2f}m²')
print(f'Para pintar a parede, será necessário {area/litro:.2f}l de tinta.')


