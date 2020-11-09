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
print(' O valor em kilometros fica {} \n e o valor em hectametros fica {} '.format((valor / 1000), (valor / 100))')
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

