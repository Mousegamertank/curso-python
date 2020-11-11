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

#AULA 09 
#cadeia de caracteres para solução de programas
#frase = 'Curso em Video Python'
#cada letra é um caracetr encluindo em espaços 
#frase[9] pega a letra na casa 9 
#frase[9:13] pega as letras até na casa 12  a partir do 9
#frase[9:21:2] do caracter 9 a 20 de 2 em dois
#frase[:5] vai de 0 a 4 
#frase[15:] vai do caracter escolhido (15) até o final
#frase[9::3] começa no 9 e vai até o final em 3 casas
#len(frase) comprimento da string
#frase.count('o') conta os o dentro da string
#frase.count('o, 0, 13') conta os O dentro da string com fatiamento
#frase.find('deo') quantidade de vezes que fez a comtagem da sring desejada / caso não exista ele -1 
#'Curso' in frase (existe a string em uma string)
#frase.replace('Python', 'Android') substitui o primeiro valor pelo segundo especificado
#frase.upper() deixa em maiusculo
#frase.lower() transforma em minusculo
#frase.capitalize() deixa o primeiro caracter em Maiscula e o resto em minusculo
#frase.title() transforma cada  palavra com o Capitalize
#frase.strip() remove os espaço inuteis no inicio e no fim
#frase.rstrip() remove somente os ultimos espaços
#frase.lstrip() remove os espaços da direita
#frase.split() divisão da string 
#'-'.join(frase) pega as strings separadas pelo split e coloca o valor desejado
#pratica aula 9
frase = '   Curso em Video Python   ' 
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15])
print(frase[::2])

print('OI')
print("""ksdjflkjasldkfjlkasjlçdjfklsjadlkfjklsajdkfjlsjadljfk
asdfasdfasdgjjjjjjjjjjjjh
sadgkjhasdkjfjasldkjfçasjdkg]kaskdhgfsjka
""")

print(frase.count('o'))
print(frase.upper().count('o')) #joga para maiuscula e deixa o o 

print(len(frase))
print(len(frase.strip()))

print(frase.replace('Python', 'Android'))
print(frase.replace('Python', 'Android'))
print(frase)

print('Curso' in frase)
print(frase.lower().find('Curso'))
print(frase.split())
divido = frase.split()
print(divido[2][3])

#aula 010
'''
condições simples e compostas
estrutura sequenciaç
carro.siga() carro é o objeto e o siga o metodo
carro.esquerda() 
carro.siga()
carro.direita()

2 possibilidades logo ele pode desviar de linhas a partir de uma decisão
condições dos programas

indentação

carro.siga()
se carro.esquerda() 
 comando1
 comando2
 comando3
senao
 comando1
 comando2
 comando3
carro.pare()

Estrutura condicional
se carro.esquerda()
 bloco_v_
senao
 bloco_f_
===
if carro.esquerda():
 bloco True
else:
 bloco False
 
tempo = int(input('Quantos anos tem seu carro?'))
if tempo <= 3:
 print('Carro novo')
else:
 print('carro velho')
print('--FIM--')

tempo = int(input('Quantos anos tem seu carro?'))
print('carro novo' if tempo<=3 else'carro velho')
print('--FIM--')
'''

nome = str(input('Qaul o seu nome?  '))
if nome == 'Pedro':
  print('Nome mais que comum')
else:
  print('Nome normal')
print('Bom dia {}!'.format(nome))
#
n1 = float(input('Digite a 1° nota  '))
n2 = float(input('Digite a 2° nota  '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))

if m >= 6.0:
  print('Sua média foi boa! Parabens')
else:
  print('Sua Média foi ruim! Estude Mais!')
#
n1 = float(input('Digite a 1° nota  '))
n2 = float(input('Digite a 2° nota  '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))

print('PARABENS' if m>= 6 else 'ESTUDE MAIS!')
