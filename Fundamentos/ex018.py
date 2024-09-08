import math
angulo=int(input('Digite um ângulo: º'))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))

print(f'O ângulo {angulo}º tem SENO {seno:.2f}\n'
      f'O ângulo {angulo}º tem COS {cos:.2f}\n'
      f'O ângulo {angulo}º tem TAN {tang:.2f}')
