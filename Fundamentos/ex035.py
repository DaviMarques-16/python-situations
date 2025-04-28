from time import sleep
print('^^^'*25)
print('\033[1;35;40mANALISADOR DE POSSIBILIDADES REFERENTE À TRIANGULOS\033[m')
print('^^^'*25)

seg1=float(input('Digite o primeiro segmento: '))
seg2=float(input('Digite o segundo segmento: '))
seg3=float(input('Digite o terceiro e último segmento: '))
print('\n')

if (seg2-seg3)<seg1<seg2+seg3 and (seg1-seg3)<seg2<seg1+seg3 and (seg1-seg2)<seg3<seg1+seg2:
    print('\033[4;31;48mLOADING...\033[m')
    sleep(1.5)
    print('\033[1;32;40mÉ possível fazer um triângulo!\033[m')
else:
    print('\033[4;31;48mLOADING...\033[m')
    sleep(1.5)
    print('\033[1;31;40mNão é possível fazer um triângulo!\033[m')

