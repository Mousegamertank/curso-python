#000
print('Olá Mundo')
n1 = input('Insira o primeiro valor')
n2 = input('Insira o segundo valor')

print(n1 + n2)

#001
#primeiro exercicio
print('Olá, Mundo')
#ou
msg = 'Olá, Mundo'
print(msg)
#-------
# print ('Olá Mundo')
print ('caso haja uma mensagem sem as aspas')

nome = 'pedro'
idade = 25
peso = 75.8
print(nome, idade, peso)
 
nome = input('Qual é seu nome')
idade = input('Qual a sua idade')
peso = input('Qual o seu peso')
print(nome, idade, peso)


#002
nome = input('Qual o seu nome?')
print('Olá' + nome + '! Prazer em te conhecer!')
#O python tem a formatação preparada logo
#print('Olá' + nome + '! Prazer em te conhecer!')
#ou
#print('Olá! Prazer em te conhecer! {}'.format(nome))
#----------------------------------
nome = input('Qual o seu nome?')
print('Olá' + nome + '! Prazer em te conhecer!')

dia = input('Informe-nos o dia de nascimento')
mes = input('Qual o mes do seu nascimento')
ano = input('Qual o ano de seu nascimento')
print('Você nasceu no dia' , dia, 'de', mes, 'de', ano, '. Correto?')

n1 = input('Informe-nos o primeiro numero')
n2 = input('Informe-nos o segundo numero')
print(n1 + n2)

#003 (desafio)
n1 = int(input('Insira o valor desejado \n'))
n2 = int(input('Insira o segundo valor desejado \n'))

print('A soma dos dois números são {}'.format(n1+n2))

#004 (desafio)
val = input('Insira o que você quiser desejado \n')

print('O tipo é: {}'.format(type(val)))

print('Retornaremos True se for verdadeiro abaixo e False se for falso \n') 
print('Somente espaços: {}'.format(val.isspace()))
print('O que foi digitado é numerico: {}'.format(val.isnumeric()))
print('O que foi digitado está em Letras Maiusculas: {}'.format(val.isupper()))
print('É alpha númerico: {}'.format(val.isalpha()))
print('É decimal: {}',format(val.isdecimal()))
print('É idenificador: {}'.format(val.isidentifier()))

#005
#inteiro com sucessor e antecessor
n1 = int(input('Insira um número inteiro \n'))

print('O sucessor é: {} \n e o antecessor é {}'.format((n1+1), (n1-1)))

#006
#ler um núemro que mostre o dobro o triplo e a raiz quadrada
n = float(input('Informe-nos o número \n'))
#dobro = n * 2
#triplo = n * 3
#raiz = n ** (1/2)

#print(' O dobro é {:.2f} \n O triplo é {:.2f} \n e a Raiz quadrada é {}'.format(dobro, triplo, raiz))
print(' O dobro é {:.0f} \n O triplo é {:.0f} \n e a Raiz quadrada é {:.2f}'.format((n * 2), (n * 3), (n ** (1/2))))


#007
#ler duas notas e mostrar a media
n1 = float(input('Insira a primeira nota \n'))
n2 = float(input('Insira a segunda nota \n'))
#media = (n1 + n2) / 2
#print('A média é: {}'.format(media))
print('A média é: {}'.format(((n1 + n2) / 2)))


#008
#Ler um valor em metros e apresentar em cm e milimetros
valor = float(input('Insira o valor em metros \n'))
#km = valor / 1000
#hc = valor / 100
#dc = valor / 10
#cm = valor * 100
#mm = valor * 1000

#print(' O valor em centimetros fica {} \n e o valor em milimetros fica {} '.format(cm, mm))
print(' O valor em kilometros fica {} \n e o valor em hectametros fica {} '.format((valor / 1000), (valor / 100)))
print(' O valor em centimetros fica {} \n e o valor em milimetros fica {} '.format((valor * 100), (valor * 1000)))


#009
#ler inteiro e mostrar tabuada
n1 = int(input('Informe o número e devolveremos a tabuada'))
'''
print('A tabuada fica:')
print('{} * 1 = {}'.format(n1, n1 * 1))
print('{} * 2 = {}'.format(n1, n1 * 2))
print('{} * 3 = {}'.format(n1, n1 * 3))
print('{} * 4 = {}'.format(n1, n1 * 4))
print('{} * 5 = {}'.format(n1, n1 * 5))
print('{} * 6 = {}'.format(n1, n1 * 6))
print('{} * 7 = {}'.format(n1, n1 * 7))
print('{} * 8 = {}'.format(n1, n1 * 8))
print('{} * 9 = {}'.format(n1, n1 * 9))
print('{} * 10 = {}'.format(n1, n1 * 10))
'''
print('-' * 12)
print('{} * {:2} = {}'.format(n1, 1, n1 * 1))
print('{} * {:2} = {}'.format(n1, 2, n1 * 2))
print('{} * {:2} = {}'.format(n1, 3, n1 * 3))
print('{} * {:2} = {}'.format(n1, 4, n1 * 4))
print('{} * {:2} = {}'.format(n1, 5, n1 * 5))
print('{} * {:2} = {}'.format(n1, 6, n1 * 6))
print('{} * {:2} = {}'.format(n1, 7, n1 * 7))
print('{} * {:2} = {}'.format(n1, 8, n1 * 8))
print('{} * {:2} = {}'.format(n1, 9, n1 * 9))
print('{} * {} = {}'.format(n1, 10, n1 * 10))
print('-' * 12)

#010
#ler o dinheiro e mostrar em dolares
din = float(input('Informe quantos reais tu tem R$ \n'))
#dol = din / 5.65
#iene = din / 0.054 Real
#euro = din / 6.61
#libras esterlinas = din / 7.30

#print('Em dolar você possui {:.2f}'.format(dol))
print('Você possui R${} em dolar você pode comprar U${:.2f}'.format(din ,(din / 5.65)))
print('Você possui R${} em dolar você pode comprar {:.2f} iene'.format(din ,(din / 0.054)))
print('Você possui R${} em dolar você pode comprar {:.2f} EU$'.format(din ,(din / 6.61)))
print('Você possui R${} em dolar você pode comprar {:.2f} libras esterlinas'.format(din ,(din / 7.30)))





#011
#pegar altura e largura de uma parede tirar a area e pintar sendo que cada galão pinta 2m²
alt = float(input('Insira a Altura \n'))
larg = float(input('Insira a Largura \n'))
#area = (alt * larg)

print('A quantidade de tinta a ser utilizada vai ser {}'.format((alt * larg)  / 2))

#012
#Ler o preço do produto e subtrair 5 %

preco = float(input('Informe-nos o valor e deixaremos com 5 porcento de desconto \n R$ '))
#descon = (preco * 5) / 100
print('O valor é de :{}'.format(preco - ((preco * 5) / 100)))
#print('O valor é de: {}'.format(preco - descon))

#013
#Ler o salario do funcionario e dar 15 porcento de aumento
sal = float(input('Informe-nos seu salario \n'))
#aumen = (sal * 15) /100

#print('Seu novo salário é: {}'.format(sal + aumen))
print('Seu novo salário é: {}'.format(sal + ((sal * 15) /100)))
      
#014
#ler em graus celsius a temperatura e passar para farenheigth
c = float(input('Informe o valor em graus celsius'))
f = (c * 9/5) + 32
print('O modelo de resposta de {} celsius é: {}'.format(c, f))

#015
#Perguntar a qauantidade de Km percorridos e dias sendo que o custo do dia é de 60:00 R$, e o de km é 0,15 R$
dia = int(input('Informe-nos a quantidade de dias alugado \n'))
km = float(input('Quantos Km Rodados \n'))
preco = (60 * dia) + (km * 0.15)

print('O total a se pagar foi de: R${:.2f}'.format(preco))

#016
# Ler um número qualaquer pelo teclado e mostrar a porção inteira
from math import trunc
x = float(input('Informe-nos o valor desejado \n'))

print('O valor inteiro é de: {}'.format(trunc(x)))
 #
num = float(input('Digite um valor'))
print('O vlaor  digitado foi {} e a sua porção foi de {}'.format(num, int(num)))

#017
#Fazer um programa para ler o comprimento do cateto oposto e do cateto adjacentte e  mostre o comprimento da hipotenusa
co = float(input('cateto oposto \n'))
ca = float(input('cateto adjacente \n'))
hip = ((co**2) + (ca**2)) **(1/2) 

print('A hipotenusa vai ser: {:.2f}'.format(hip))

import math 
co = float(input('cateto oposto \n'))
ca = float(input('cateto adjacente \n'))
hi = math.hypot(co, ca)

print('A hipotenusa vai medir {:.2f}'.format(hi))

#018
#Programa que leia um ângulo qualquer e mostre na tela o valor do seno, cossno e tangente desse ângulo
import math
angu = float(input('Informe-nos o angulo \n'))
angu = math.radians(angu)
sen = math.sin(angu)
cos = math.cos(angu)
tan = math.tan(angu)
print('O angulo de {} tem o Seno de {:.2f}'.format(angu, sen))
print('O angulo de {} tem o Coseeno de {:.2f}'.format(angu, cos))
print('O angulo de {} tem a Hipotenusa de {:.2f}'.format(angu, tan))

#019
#sortear 4 alunos para apagar o quadro, um programa que ajude ele , lendo o nome e escrevendo o nome do escolhido
import random
alunos = []
for i in range(4):
  alunos.append(input('Informe-nos o nome do aluno \n'))

print('O aluno que vai apagar a lousa é {}'.format(random.choice(alunos)))

#\\\\\\\\\\\\\
aluno1 = input('1° aluno \n')
aluno2 = input('2° aluno \n')
aluno3 = input('3° aluno \n')
aluno4 = input('4° aluno \n')

print('O aluno que vai apagar a lousa é {}'.format(random.choices(alunos)))

#020
#Pegar o programa anterior e sortear a ordem dos alunos randomicamente mostrando a ordem
import random
alunos = []
for i in range(4):
  alunos.append(input('Informe-nos o nome do aluno \n'))

random.shuffle(alunos)
print('O aluno que vai apagar a lousa é {}'.format(alunos))

from random import shuffle
alunos = []
for i in range(4):
  alunos.append(input('Informe-nos o nome do aluno \n'))

shuffle(alunos)
print('O aluno que vai apagar a lousa é {}'.format(alunos))

#021 
#fazer um programa que reproduza um arquivo MP3
# Fazer em casa

#022
#ler o nome do usuario completo e mostrar:
#O nome com todas as letras maisculas, com as letras minusculas, quantas letras sem considerar espaço, e quantas letras tem o primeiro nome
nome = str(input('Informe o sue nome \n')).strip()

print('o nome em maiuculos vai ser {}'.format(nome.upper()))
print('o nome em minusculos vai ser {}'.format(nome.lower()))
print('o nome em quantas letras sem espaços vai ser {}'.format(len(nome)- nome.count(' ')))
#print('o nome em letras no primeiro nome vai ser {}'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro no é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

#023 
#ler um número de 0 a 9999 e mostra cada um dos digitos separados, ex: 1834
#unidade: 4; dezena: 3; centena: 8; milhar: 1
#023
#ler um número de 0 a 9999 e mostra cada um dos digitos separados, ex: 1834
#unidade: 4; dezena: 3; centena: 8; milhar: 1
x = int(input('Informe o numero \n'))
n = str(x)

print('a unidade é: {}'.format(n[3]))
print('a dezena é: {}'.format(n[2]))
print('a centena é: {}'.format(n[1]))
print('o milhar é: {}'.format(n[0]))

#
x = int(input('Informe o numero \n'))

u = x // 1 % 10
d = x // 10 % 10
c = x // 100 % 10
m = x // 1000 % 10

print('a unidade é: {}'.format(u))
print('a dezena é: {}'.format(d))
print('a centena é: {}'.format(c))
print('a centena é: {}'.format(m))

#024
#ler o nome de uma cidade e ver se tal começa com 'SANTO'  
cidade = str(input('Informe o nome da sua cidade \n')).strip()
cidade = cidade.lower()
cidade = cidade[:5]

print('se o valor a seguir for -1 sua cidade não começa com santo \n {}'.format(cidade.find('santo')))

#
cidade = str(input('Informe o nome da sua cidade \n')).strip()
cidade = cidade.capitalize()
print(cidade[:5] == 'Santo')

#
cidade = str(input('Informe o nome da sua cidade \n')).strip()
print(cidade[:5].capitalize() == 'Santo')


#025
#ler o nome de uma pessoa e dizer se possue o SILVA
#ler o nome de uma pessoa e dizer se possue o SILVA
nome = str(input('Informe o seu nome completo \n')).strip()
nome = nome.title()
print('Silva' in nome)

#026
#ler uma frase qualquer e mostrar
#quantas vezes aparece a letra A, em que posição ela aprece na primeira, e que posição ela aparece na ultima
#026
#ler uma frase qualquer e mostrar
#quantas vezes aparece a letra A, em que posição ela aprece na primeira, e que posição ela aparece na ultima

frase = str(input('Informe a Frase \n')).strip()
frase = frase.upper()
print('existem {} "A"'.format(frase.count('A')))
print('ela aparece na posição {}'.format(frase.find('A')+1))
print('ela aparece na posição {}'.format(frase.rfind('A')))



#027
#ler o nome completo mostrar o primeito e o ultimo nome separados ex: Ana maria de Souza
#Ana, Maria
#027
#ler o nome completo mostrar o primeito e o ultimo nome separados ex: Ana maria de Souza
#Ana, Maria
nome = str(input('Informe o nome completo \n')).strip()
nome = nome.split()
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu ultimo nome é: {}'.format(nome[len(nome)-1]))

#028 - escreva um programa pensar em um numero inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual foi o numero escolhido pelo computador mostrae se venceu ou perder
import random
n = [1, 2 ,3 ,4 , 5]
n = random.choice(n)

nUsuario = int(input('Informe o numero entre 1 a 5 \n'))
if (nUsuario == n):
  print('Está Correto')
else:
  print('Está Errado')
  
#
from random import randint
from time import sleep

computador = randint(0, 5)

print('=*=' * 20)

nusu = int(input('Informe o numero entre 1 a 5 \n'))

sleep(2) #faz o computador dar uma paradinha

if (computador == nusu):
  print('Está Correto')
else:
  print('Está Errado')
print('=*=' * 20)



#029 - ler a velocidade de um carro, se passar 80km/h foi multado se não ultrapassar mostra nada, a multa vai ser R$7.00 por cada Km acima do limite
velocidade = float(input('Informe a velocidade do carro(já está em km) \n'))

if velocidade > 80:
  diferença = velocidade - 80
  diferença *= 7.00
  print('A sua multa será de: R${:.2f}'.format(diferença))
else:
  print('Parabens pela conduda perante ao volante')
  
#030 - numero par ou impar o usuario digita o numero
num = int(input('Informe um número inteiro, ex:1, 2... \n'))

if num % 2 == 0:
  print('O número {} é par'.format(num))
else:
  print('O número {} é impar'.format(num))
   
#031 - distancia de uma viagem em KM calcule o preço da passagem, cobrando R$0.50 por KM para viagens de até 200km e R$0.45 para viagens mais longas
km = float(input('Informe a distancia (já está em kilometros) \n'))

if km <= 200:
  print('O valor da sua passagem será de: {:.2f}'.format(km * 0.50))
else:
  print('O valor da sua passagem será de: {:.2f}'.format(km * 0.45))

#032 - faça um programa qualquer e mostre se é bissexto
ano = str(input('Informe o ano \n'))
anof = int(ano)
un = ano[-1]
de = ano[-2]
ano = de + un
ano = int(ano)

if (ano % 4 == 0):
  print('O ano {} é bissexto'.format(anof))
else:
  print('O ano {} não é bissexto'.format(anof))
  
#033 - faça um programa que leia 3 números qual o maior e o menor
n1 = int(input('Informe o 1° número'))
n2 = int(input('Informe o 2° número'))
n3 = int(input('Informe o 3° número'))

if n1 > n2 and n1 > n3:
  print('O {} é o maior número'.format(n1))
if n2 > n1 and n2 > n3:
  print('O {} é o maior número'.format(n2))
if n3 > n2 and n1 < n3:
  print('O {} é o maior número'.format(n3))

#034 - pedir o salario para o funcionario se for superior a 1.250,00 aumentar 10%, senão aumento de 15%
salario = float(input('Informe-nos o seu salário: R$ '))

if salario >= 1250.00:
  salario = ((salario * 10) / 100) + salario
else:
  salario = ((salario * 15) / 100) + salario

print('Seu novo salário é: {:.2f}'.format(salario))

#035 - ler tres retas e informar se é um triangulo 
 
