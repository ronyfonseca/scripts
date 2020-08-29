import socket
print('='*20)
print('[1]PortScan\n[2]Calculadora\n[3]Quiz')
print('='*20)
r1 = int(input('Escolha uma opção:'))
if (r1 == 1):
    t1 = str(input('Digite o site com EX. eu.com:'))
    portas = [21, 23, 80, 443, 8080]
    for porta in portas:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.settimeout(0.1)
        codigo = cliente.connect_ex(('{}'.format(t1), porta))
        if (codigo == 0):
            print("Aberta", porta )
if (r1 == 2):
    print("""
         ____________________
          RESULTADO:        
         |------------------|
         |[7]|[8]|[9]|[ - ] |
         |[4]|[5]|[6]|[ % ] |
         |[1]|[2]|[3]|[ + ] |
         |[0]|[0]|[.]|[ENTER|
         |__________________|
         """)
    n1 = int(input('Digite o primeiro número:'))
    n2 = str(input('Você que somar + ou subtrair - ou dividir % ?:'))
    n3 = int(input('Digite o segundo numero:'))
    if (n2=='+' ):
        t1 = n1 + n3
        print("""
         ____________________
          RESULTADO:{}      
         |------------------|
         |[7]|[8]|[9]|[ - ] |
         |[4]|[5]|[6]|[///] |
         |[1]|[2]|[3]|[ + ] |
         |[0]|[0]|[.]|[ENTER|
         |__________________|
         """.format(t1))
    elif (n2=='-'):
        r2 = n1 - n3
        print("""
         ____________________
          RESULTADO:{}      
         |------------------|
         |[7]|[8]|[9]|[ - ] |
         |[4]|[5]|[6]|[///] |
         |[1]|[2]|[3]|[ + ] |
         |[0]|[0]|[.]|[ENTER|
         |__________________|
         """.format(r2))
    elif (n2=='%'):
        r3 =  n1 / n3
        print("""
         ____________________
          RESULTADO:{:.2f}  
         |------------------|
         |[7]|[8]|[9]|[ - ] |
         |[4]|[5]|[6]|[///] |
         |[1]|[2]|[3]|[ + ] |
         |[0]|[0]|[.]|[ENTER|
         |__________________|
         """.format(r3))
if (r1==3):
    print('')
print('='*67)
print('Bem vindo ao meu quiz')
print('='*60)
n1 = int(input('Qual minha idade?:'))
if (n1==15):
    print('+1 ponto\n')
    r1 = 1
else:
    print('0 pontos\n')
    r1 = 0


n2 = str(input('Qual o meu nome?:'))
if (n2=='Rony'):
    print('+1 ponto\n')
    r3 = r1 + 1
elif(n2=='rony'):
    print('Falta a letra maiúscula no começo\n0 pontos\n')
    r3 = r1 + 0
else:
    print('0 ponto\n')
    r3 = r1 + 0


n3 = str(input('Qual minha linguagem de programação?:'))
if (n3=='Python'):
    print('+1 ponto\n')
    r4 = r3 + 1
elif (n3=='python'):
    print('Meu deus letra maiúscula no começo preste atenção!\n0 pontos\n')
    r4 = r3 + 0
else:
    print('0 pontos\n')
    r4 = r3 + 0


n4 = str(input('Qual meu segundo nome hacker?:'))
if (n4=='Bruno'):
    print('+1 ponto\n')
    r5 = r4 + 1
elif (n4=='bruno'):
    print('Presta atenção letra maiúscula nos nomes e começos de frase!\n0 ponto\n')
    r5 = r4 + 0
else:
    print('Meu nome no mundo hacker é Bruno!')
    print('0 ponto')
    r5 = r4 + 0

n5 = int(input('Eu fiquei quantos dias sem programar por conta do pc quebrado?:'))
if (n5==4, 5, 6):
    print('+1 ponto\n')
    r6 = r5 + 1
elif (n5 >= 7):
    print('Na verdade foram 4 dias sem contar segunda\n0 ponto\n')
    r6 = r5 + 0
else:
    print('0 ponto\n')
    r6 = r5 + 0
print('-'*60)
n6 = (r6)
if (n6 >= 5):
    print('Você é meu melhor amigo!')
    print('TOTAL DE PONTOS:{}'.format(n6))
elif (n6 <= 4):
    print('Você não sabe muito sobre mim!\nTOTAL DE PONTOS:{}'.format(n6))
print('-'*67)
print('='*80)
