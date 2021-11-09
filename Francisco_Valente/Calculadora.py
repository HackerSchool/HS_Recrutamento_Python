def Nível_3():
  print('''
        Escolhe dois números:
        Número 1
        Número 2
        ''')
  n1=float(input())
  n2=float(input())
  print('''
        Define  tua operação:
        1-Adição
        2-Subtração
        3-Divisão
        4-Multiplicação
        5-Quociente
        6-Exponenciação
        ''')
  opcao=input()
  if opcao=='1' :
    ad=n1+n2
    print(ad)

  elif opcao=='2' :
    sub=n1-n2
    print(sub)

  elif opcao=='3' and n2!=0:
    div=n1/n2
    print(div)

  elif opcao=='3' and n2==0:
    print('Math Error')

  elif opcao=='4' :
    mult=n1*n2
    print(mult)

  elif opcao=='5' and n2!=0:
    quo=n1%n2
    print(quo)
    
  elif opcao=='5' and n2==0:
    print('Math Error')
    
  elif opcao=='6' :
    exp=n1**n2
    print(exp)

  elif opcao!=['1','2','3','4','5','6']:
    print('Invalid input, try a valid input')

def Nível_5():
  print('Define a tua expressão:')
  e=input()
  if '+' in e:
    e=e.split('+')
    #print(e)
    print(float(e[0])+float(e[1]))
  if '-' in e:
    e=e.split('-')
    #print(e)
    print(float(e[0])-float(e[1]))
  if '*' in e and (list(e).count('*'))<2:
    e=e.split('*')
    #print(e)
    print(float(e[0])*float(e[1]))
  if '%' in e and (list(e).count('0'))<1:
    e=e.split('%')
    #print(e)
    print(float(e[0])%float(e[-1]))
  if '%' in e and (list(e).count('0'))>0:
    print('Math Error')
  if '**' in e and (list(e).count('*'))>1:
    e=e.split('**')
    #print(e)
    print((float(e[0]))**(float(e[1])))
  if '/' in e and (list(e).count('0'))<1:
    e=e.split('/')
    #print(e)
    print(float(e[0])/float(e[-1]))
  if '/' in e and (list(e).count('0'))>0:
    print('Math Error')
    
def calculator():
  while 1==1:
    print('''
Calculadora 101          
        Escolhe uma opção:
        1-Nível 3
        2-Nível 5
        3-Sair
        ''')
    opção=input()
  
    if opção=='1':
      Nível_3()

    elif opção=='2' :
      Nível_5()

    elif opção=='3' :
      print('A Sair')
      break

    elif opção!=['1','2','3']:
      print('Input not accepted')

