#https://docs.python.org/3.8/tutorial/index.html

#PRINT NORMAL
print('Olá mundo!!')
print(1)
nome = "mari"
print("Olá, " + nome)
print("7 + 4")
print("7" + "4")
print(7 + 4)
print(7 , 4)
print("ola" , 7 ,5)
print("ola" + 7 +5) #Essa dará errado 

#PRINT SALVANDO NA VARIAVEL
nome1 = "Arthur"
idade = 18
peso = 75.1
print(nome1, idade, peso)
print(nome1 + idade + peso) #dessa forma ele n deixa porq n entende como concatenar com int 

#PRINT USANDO A FUNÇÃO INPUT

nome = input("Digite seu nome por favor: ")
idade = input("Digite sua idade: ")
peso = input("Digite seu peso: ")
print("Olá, " + nome)
print("Olá, " + nome ,"você tem" ,idade ,"anos e você pesa" , peso ,"kg")
print("Olá, " , nome ,"você tem" ,idade ,"anos e você pesa" , peso ,"kg") #ele entende tbm poq são strings

#USANDO O PRINT FORMATADO

nome = input("Digite seu nome por favor: ")
idade = input("Digite sua idade: ")
peso = input("Digite seu peso: ")
print("Olá {}, você tem {} anos e você pesa {} kg" .format(nome, idade, peso))


a = 1
print(type(a))
a = 'Mariane'
print(type(a))
a = True
print(type(a))
a = 1 - 5j
print(type(a))
n3 = 7
print(type(n3))
n4 = 7.0
print(type(n4))

#USANDO O INPUT DIZENDO O TIPO DE VARIAVEL, NO CASO INT, FLOAT

n1 = input("digite um valor: ")
n2 = input("Digite um valor: ")
s = n1 + n2
print(type(s))
print(s)

n1 = int(input("digite um valor: "))
n2 = int(input("Digite um valor: "))
s = n1 + n2
print(type(s))
print(s)
#SEM O .FORMAT
print ("A soma entre " , n1 , "e " , n2 , "vale ", s)
#COM O .FORMAT
print("a soma do numero {} e do numero {} resulta no numero de {}".format(n1,n2,s))

#SEM VARIAVEL
print("a soma do numero {} e do numero {} resulta no numero de {}".format(n1,n2,(n1+n2)))

n4 = bool(input("digite um valor: "))
print(n4) #SE N DIGITAR VALOR ELE ENTENDE QUE É FALSO
n5 = float(input("digite um valor: "))
print(n4)

#USANDO AS FUNCOES PARA SABER O TIPO DA VARIAVEL MESMO USANDO O INPUT

n = input("Digite algo: ")
print(n.is)
print(n.isnumeric()) #verifica se é numérico
print(n.isalpha()) #verifica se é letra
print(n.isspace()) #se é só espaço
print(n.isalnum()) # se é alpha numerico por exemplo 3a
print(n.isupper()) # se esta em letras maiusculas
print(n.islower()) # se esta em letras minuscula
print(n.istitle()) # palavra capitalizada por exemplo, Python 

#TIPOS DE OPERAÇÕES

print(17/3) #DIVISÃO NORMAL
print(17//3) # RESULTADO DA DIVISÃO SEM USAR A VIRGULA (INTEIRO)
print(5**2) #POTENCIA
print(pow(2,3)) #POTENCIA USANDO A FUNÇÃO INTERNA, PORÉM PERDE A ORDEM DE PROCEDENCIA
print(6%2) #RESTO DA DIVISÃO
print(13%5)
print(5*2)
print(50 - 5*6/4) 
print((50-5*6)/4) # RESOLVE PRIMEIRO O PARENTESES

#RESOLVENDO RAIZ QUADRADA

n1 = 81**(1/2)
n2 = 81**0.5
print(n2)
print(n1)

#COISAS QUE O PYTHON ACEITA
print("Oi" *5)
print("=" *20)


nome = input("Digite seu nome por favor: ")
print("Olá, foi um prazer te conhecer {}!".format(nome))
print("Olá, foi um prazer te conhecer {:20}!".format(nome)) #usar 20 espaços
print("Olá, foi um prazer te conhecer {:>20}!".format(nome)) #alinhado a direita
print("Olá, foi um prazer te conhecer {:<20}!".format(nome)) #alinhado a esquerda
print("Olá, foi um prazer te conhecer {:^20}!".format(nome)) #alinhado ao centro
print("Olá, foi um prazer te conhecer {:=<20}!".format(nome)) #colocando iguais


n1 = float(input("digite um valor: "))
n2 = float(input("Digite um valor: "))
print("a divisão do numero {} e do numero {} resulta no numero de {:.3f}".format(n1,n2,(n1/n2))) 
print("a divisão do numero {} e do numero {} resulta no numero de {:.2f}".format(n1,n2,(n1/n2))) 
#FORMATANDO O NUMERO DE CASAS 

#CASO EU QUEIRA OS PRINTS NA MESMA LINHA

n1 = float(input("digite um valor: "))
n2 = float(input("Digite um valor: "))
print("a divisão do numero {} e do numero {} resulta no numero de {:.3f}".format(n1,n2,(n1/n2)), end=" >>>") 
#também posso por coisas dentro do end q ele irá printar
print("a soma do numero {} e do numero {} resulta no numero de {}".format(n1,n2,(n1+n2))) 
 #O END PERMITE O PRINT NÃO FAZER A QUEBRA DE LINHA
 
 
 #CASO EU QUEIRA UM UNICO PRINT EM LINHAS SEPARADAS LINHA USO O \n
 
n1 = float(input("digite um valor: "))
n2 = float(input("Digite um valor: "))
s = n1+n2
d = n1/n2
m = n1*n2
print("o resultado divisão é {}, \n e o resultado da soma é {}, \n e o resultado da multiplicação é {}".format(d,s,m))
      