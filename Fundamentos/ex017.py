'''import math
catop=float(input('Qual comprimento do cateto oposto? '))
catadj=float(input('Qual comprimento do cateto adjacente? '))

hip = math.hypot(catop,catadj)

print(f'O valor da hipotenusa é {hip:.2f}')'''

catop=float(input('Qual comprimento do cateto oposto? '))
catadj=float(input('Qual comprimento do cateto adjacente? '))
hip2 = catop**2+catadj**2
hip = hip2**(1/2)

print(f'O valor da hipotenusa é {hip:.2f}')
