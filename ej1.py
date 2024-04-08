import random

matriz = [
  ["-","-","-","-"],
  ["-","-","-","-"],
  ["-","-","-","-"],
  ["-","-","-","-"]
]

def llenar (matriz):
  for f in range(0,len(matriz)):
    for c in range(0,len(matriz[0])):
      print("ingrese un numero")
      num = input()
      if num.isdigit():
        bien = 1
      else:
        print("no ingresaste un numero , ingrese otro")
        num = input()
      matriz[f][c] = int(num)
  
  return matriz

print(llenar(matriz))

signo = "#"

def aleatorio(matriz,signo):
  fila = random.randint(0,len(matriz)-1)
  columnas = random.randint(0,len(matriz)-1)
  matriz[fila][columnas] = signo

  return matriz,fila,columnas


print(aleatorio(matriz,signo))

def buscar(matriz,signo):
  intentos = 0
  terminar = 0
  for f in range(0,len(matriz)+1):
    intentos = f
    if terminar == 1 :
      break
    for c in range(0,len(matriz[0])):
      if matriz[f][c] == signo:
        terminar = 1
        print(f"su signo esta en la pocicion " + str(f) + " "+" "+ str(c))
        break
  print(f"intentaste buscar el signo " + str(intentos) + " veses")
  return intentos

print(buscar(matriz,signo))
