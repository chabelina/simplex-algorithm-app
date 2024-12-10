import numpy as np
import os
import time

# Leer función objetivo (FO) y restricciones.

# Funcion para leer matrices de dimension determinable
def leerMatriz(i, j):
  valores = list(map(int, input("Ingresa los elementos de la matriz: ").split()))

  matriz = np.array(valores).reshape(i,j)
  return matriz

def hallarVarNB(vB, varTotal):
  # Create a set of all variables (from 1 to total_vars)
  all_vars = set(range(1, varTotal + 1))

  # Convert the basic variables to a set
  set_vB = set(vB)

  # Find the non-basic variables by subtracting the basic variables from the set of all variables
  vNB = list(all_vars - vB)

  # Sort the non-basic variables (optional, for better order)
  vNB.sort()

  return vNB

def main():
  print("*****************")
  print("ALGORITMO SIMPLEX")
  print("*****************")
  input ("[Presiona ENTER]")

  os.system('cls')

  num_var = int(input("Ingresa el numero de variables de la FO: "))

  print("Ingresa los coeficientes de la FO (c): ")
  c = leerMatriz(1, num_var)

  num_rstrc = int(input("Ingresa el numero de restricciones: "))

  num_varTotal = num_var+num_rstrc
  
  print("Ingresa la matriz de coeficientes de las restricciones (A): ")
  A = leerMatriz(num_rstrc, 3)

  print("Ingresar el lado derecho de las restricciones (b): ")
  b = leerMatriz(num_rstrc, 1)

  os.system('cls')

  vB = leerMatriz()
  
  simplex(c, A, b, num_rstrc, num_var)

main()


def simplex(c, A, b, numRestric, numVar, vB, vNB):
  return