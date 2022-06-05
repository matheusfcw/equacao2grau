# escrita na forma: ax^2+bx+c
# formula de deltaΔ: b^2-4ac
# formula de resolução: (-b+-√Δ)2a
import math
import time
from xml.sax import default_parser_list
print('-----------')
print('Para descobrir o valor dos coeficientes, use com base isso ax²+bx+c')
print('Lembre-se: a ≠ 0 e a, b, c ∈ ℝ e quando não estiver o valor de c, ele equivale a 0, o mesmo com o valor de b')
print('Quando não se tem um numero antes da incognita X o valor é 1')
varlA = int(input('Digite o valor de a: '))
varlB = int(input('Digite o valor de b: '))
varlC = int(input('Digite o valor de c: '))
soma = round(-(varlB) / ((varlA)), 2)
multi = round(varlC / varlA, 2)
delta = varlB**2-4*varlA*varlC
if delta < 0:
    resultado = ('Essa equação não pertence a os números reais')
if delta > 0:
    resultado1 = round((-(varlB)+math.sqrt(delta)) /((varlA*2)), 2)
    resultado2 = round((-(varlB)-math.sqrt(delta)) /((varlA*2)), 2)
if delta == 0: 
    resultado = (-varlB) / ((varlA*2))
# colocando os sinais
if varlA == 1:
    varlA = ' '
if varlB > 0:
    varlB = '+{}'.format(varlB)
if varlC > 0:
    varlC = '+{}'.format(varlC)
# formatando a equação
if varlC == 0:
    quest = str(input('A raiz é assim {}x²{}x=0? '.format(varlA,varlB)))
if varlB == 0:
    quest = str(input('A raiz é assim {}x²{}=0? '.format(varlA,varlC)))
if varlB != 0 and varlC != 0:
    quest = str(input('A raiz é assim {}x²{}x{}=0? '.format(varlA,varlB,varlC)))
# respondendo pergunta
if quest == 'yes' or quest == 'sim' or quest == 's':
    print('Que ótimo! Estamos calculando aguarde um pouco')
    print('...')
    time.sleep(2)
    print('O delta dessa função é {}'.format(delta))
    if delta == 0: 
        print('A raiz dessa função é {}'.format(resultado))
    if delta > 0:
        print('As raizes dessa função são {}, {}'.format(resultado1, resultado2))
        print('E a soma das raizes é {}, e sua multiplicação é {}'.format(soma, multi))
    if delta < 0:
        print('Não tem raiz para essa função, ou seja x ∉ ℝ')
if quest == 'no' or quest == 'não' or quest == 'n':
    print('Que pena!, iremos melhorar :(')