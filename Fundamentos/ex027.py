nome = str(input('Qual seu nome completo? '))
primeiro = nome.split()[0]
ultimo = nome.rsplit(' ', 15)[-1]

print(f'Seu primeiro nome é {primeiro}.\n'
      f'Seu último nome é {ultimo}.')


