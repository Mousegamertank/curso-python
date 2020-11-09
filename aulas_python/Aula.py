#Aulas totais
#------------------------------------------------------------------------
#aula 6
#A
n1 = int(input('Digite um valor \n'))
#print(type(n1))
n2 = int(input('Digite o segundo valor \n'))

s = n1 + n2
#format python 3
print('A soma entre {} e {} vale {}'.format(n1, n2, s))

#B
n = (input('Digite um valor'))
#os IS só funcionam com string
print(n.isnumeric())
#isnumeric() se é numero
#isalpha() se é letras
#isalanum() ver se é alfanumerico

#caso haja valor sera true, caso não sera false em valors booleanos

#-----------------------------------------------------------------------
#aula7
# + adição (5 + 2 == 7)
# - subtração (5 - 2 == 3)
# / divisão (5 / 2 == 2.5)
# * Multiplicação (5 * 2 == 10)
# ** potencia (5 ** 2 == 25)
# pow(x, y) [x o número embaixo e y o valor a ser elevado], operação semelhante a potencia sem o **
# raiz quadrada desejada pode ser (x**(1/2)) ou raiz cubica (x**(1/3))
# // divisão inteira (5 // 2 == 2 [pega o valor sem a virgula])
# % resto da divisão (5 % 2 == 1 [pega o resto da divisão])
# == teste o igual

#Ordem (1 _ (); 2 _ **; 3 _ *, /, //, %[faz o que aparecer primeiro]; 4 _ +, -)

#------------------------------------------------------------------------
exem1 = int(5 + 3 * 2) # == 11
exem2 = int(3 * 5 + 4**2) # == 31
exem3 = int(3 * (5 + 4) ** 2) # == 243

#print('Exemplos a se testar {}, {}, {}'.format(exem1, exem2, exem3))

#********************************
#CASO HAJA ALGO A SER REPETIDO NO PYTHON VC PODE FAZER ('oi' * 5 == 'oioioioioi' ou '=' * 20 == '===================')
#********************************

print('=' * 20)

#//////////////////////////////
#nome = input('Qual seu nome')
#print('olá {:20}!'.format(nome))
# : para formatar a quandtidade de caracteres, e logo após < para alinha a diireita, o > esquerda, o ^ centralziado e ainda colocando os valores desejados como {:=^20}
#//////////////////////////////

n1 = int(input('Um valor'))
n2 = int(input('Outro valor'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {}, \n produto {}, \n divisão{:.2f} '.format(s, m, d), end='')
print('Divisão inteira {} e potencia {}'.format(di, e))

#aula 008
#modulos, pacotes, conjuntos de funções 
'''
python vem com pacotes basicos, chamadas de bibliotecas; e assim importar modulos;
import(importa todas os recursos da biblioteca)
from (chama a biblioteca desejada) import (seleciona as funçoes dentro da biblioteca)

import math (ppega toda a biblioteca)
ceil  (arredonda para cima)
floor (arredonda para baixo)
trunc (elimina os elementos pós virgula)
pow   (potencia)
factorial (fatorial)
sqrt  (raiz quadrada)

from math import sqrt (escolhe qual a função vai ser utilizada)
from math import sqrt, ceil

#Pratica da Aula 008

import math
num = int(input('Digite um úmero: '))
raiz = math.sqrt(num)

print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))
print('A raiz de {} é igual a {}'.format(num, math.floor(raiz)))

from math import sqrt, floor
num = int(input('Digite um úmero: '))
raiz = sqrt(num)

print('A raiz de {} é igual a {}'.format(num, floor(raiz)))

import random (biblioteca me da um valor aleatorio)
num = random.random() [float entre 0 e 1]
print(num)
randint(x, y) [gera um número inteiro]

#bibliotecas para emoji
import emoji
print(emoji.emojize('Olá Mundo :sunglasses:', use_aliases="True"))
print(emoji.emojize('Olá Mundo :earth_americas:', use_aliases="True"))
 				(Nome do emoji)
'''





