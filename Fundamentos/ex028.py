import random
from time import sleep
jogo = random.randint(0, 5)
print('=='*30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('=='*30)
aposta = int(input('Faça sua aposta: '))
print('LOADING...')
sleep(2)

if aposta == jogo:
    print('Porra bicho, acertou!')
else:
    print(f'Serve nem pra acertar 1 de 6 opções...\n'
          f'Pensei no número {jogo}.')
