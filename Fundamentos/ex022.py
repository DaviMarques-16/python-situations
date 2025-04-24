nome = input('Qual seu nome completo? ')
letras = len(nome) - nome.count(' ')
nome1 = nome.find(' ')
separa = nome.split()

print(f'Seu nome completo em maiúsculo: {nome.upper()}.\n'
      f'Seu nome completo em minúsculo: {nome.lower()}.\n'
      f'Seu nome tem {letras} letras.\n'
      f'Seu primeiro nome tem {len(separa[0])} letras.')
      #f'Seu primero nome tem {nome1} letras.')
