import matplotlib.pyplot as plt
import numpy as np
import re


def calcular(vetordummy, lenght):
    
    i=0
    while(i < lenght):
        if(vetordummy[i] == '^'):
            vetordummy[i-1] = str(float(vetordummy[i-1]) ** float(vetordummy[i+1]))
            del vetordummy[i:i+2]
            lenght = len(vetordummy)
            i = i-1
            
        i += 1
    
    i=0
    while(i < lenght):
        if(vetordummy[i] == '/'):
            vetordummy[i-1] = str(float(vetordummy[i-1]) / float(vetordummy[i+1]))
            del vetordummy[i:i+2]
            lenght = len(vetordummy)
            i = i-1
        if(vetordummy[i] == '*'):
            vetordummy[i-1] = str(float(vetordummy[i-1]) * float(vetordummy[i+1]))
            del vetordummy[i:i+2]
            lenght = len(vetordummy)
            i = i-1
            
        i += 1
    
    i=0
    while(i < lenght):
        if(vetordummy[i] == '+'):
            
            vetordummy[i-1] = str(float(vetordummy[i-1]) + float(vetordummy[i+1]))
            del vetordummy[i:i+2]
            lenght = len(vetordummy)
            i -= 1
        if(vetordummy[i] == '-'):

            vetordummy[i-1] = str(float(vetordummy[i-1]) - float(vetordummy[i+1]))
            del vetordummy[i:i+2]
            lenght = len(vetordummy)
            i -= 1
            
        i += 1
    
        
        
    return(vetordummy[0])
        
def calc(vetor):

  teste = vetor
  del teste[0:2]
  del teste[-1]
  print("A calcular...")
  print(teste)

  i = len(teste)-1
        
  while(i > -1) :
    if(teste[i] == '('):
            
      j = i
      while(teste[j] != ')'):
        lenght = lenght + 1
        j = j + 1
                
      vetordummy = teste[i+1:i+lenght]
      print(vetordummy)
      teste[i] = calcular(vetordummy, len(vetordummy))
      del teste[i+1:i+lenght+1]
      print(teste)
      i = len(teste)
    i -= 1
    lenght = 0
                
  print("Resultado final:\n")            
  print(calcular(teste, len(teste)))

def eq(teste2):

  
  if(teste2[5] == ','):
    a = float(teste2[2])
    b = float(teste2[4])
    c = float(teste2[6])
    x_1 = (-b + (b**2-4*a*c)**0.5)/2*a
    x_2 = (-b - (b**2-4*a*c)**0.5)/2*a
    print("O resultado é:\n")
    print("x = ", x_1, " ou ", x_2, "\n")
  if(teste2[5] == ']'):
    a = float(teste2[2])
    b = float(teste2[4])
    x = -b/a
    print("O resultado é:\n")
    print("x = ", x, "\n")
  

  
def graph(teste3):

    if(teste3[2] == 'sin'):
      # Creating vectors X and Y
      x = np.linspace(-2, 2, 100)

      s = "sin(x)"
      y = np.sin(x)

      fig = plt.figure(figsize = (10, 5))

      plt.plot(x, y)
 

      plt.show()
    if(teste3[2] == 'cos'):
      # Creating vectors X and Y
      x = np.linspace(-2, 2, 100)

      s = "cos(x)"
      y = np.cos(x)

      fig = plt.figure(figsize = (10, 5))

      plt.plot(x, y)
 

      plt.show() 
    if(teste3[2] == 'exp'):
      # Creating vectors X and Y
      x = np.linspace(-2, 2, 100)

      s = "exp(x)"
      y = np.exp(x)

      fig = plt.figure(figsize = (10, 5))

      plt.plot(x, y)
 

      plt.show()
    if(teste3[2] == 'sqrt'):
      # Creating vectors X and Y
      x = np.linspace(-2, 2, 100)

      s = "sqrt(x)"
      y = np.sqrt(x)

      fig = plt.figure(figsize = (10, 5))

      plt.plot(x, y)
 

      plt.show()
    if(teste3[2] == 'log'):
      # Creating vectors X and Y
      x = np.linspace(-2, 2, 100)

      s = "log(x)"
      y = np.log(x)

      fig = plt.figure(figsize = (10, 5))

      plt.plot(x, y)
 

      plt.show() 
      
 

def yo():

  
  f = open("calculadora.txt", 'a+')
  f.seek(0)
  for line in f:
    if(re.split(r'([`\[\]])', line)[0] == 'calc'):
      teste1 = re.split(r'([`\-=^&*()_+\[\]{};\'\\:"|,/])', line)
      while '' in teste1: teste1.remove('')
      
      calc(teste1)
    if(re.split(r'([`\[\]])', line)[0] == 'eq'):
      teste2 = re.split(r'([`\=^&*()_+\[\]{};\'\\:"|,/])', line)
      while '' in teste2: teste2.remove('')
      eq(teste2)
    if(re.split(r'([`\[\]])', line)[0] == 'graph'):
      teste3 = re.split(r'([`\-=^&*()_+\[\]{};\'\\:"|,/])', line)
      while '' in teste3: teste3.remove('')
      graph(teste3)


  f.close()
      