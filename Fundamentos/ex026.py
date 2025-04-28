nome = str(input('Digite o nome completo: ')).strip().upper()
lyricA = nome.count('A')
firstA = nome.find('A')
lastA = nome.rfind('A')

print(f'A letra A aparece {lyricA} vezes na frase.\n'
      f'A letra A aparece a primeira vez na posição {firstA+1}\n'
      f'A letra A aparece a última vez na posição {lastA+1}.')
