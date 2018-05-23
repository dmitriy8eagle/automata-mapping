import math
import numpy as np

def make_formula_executable(formula):
  COMMANDS = [ 'pow', 'sqrt']
  BOOLEAN = {'XOR': '^', 'OR': '|', 'AND': '&'}
  
  for command in COMMANDS:
    formula = formula.replace(command, command)

  for key, value in BOOLEAN.items():
    formula = formula.replace(key, value)

  formula = formula.replace('x', 'int(x)')

  return formula

def makeArrayTmpX(mode, k, n):
  size = k if mode == 0 else k + n
  return [int(x) for x in range(2**size)]

def makeArrayTmpY(tmpX, formula):
  return [eval(formula) for x in tmpX]

def makeXArray(tmpArr, k):
  return [el%2**k / 2**k for el in tmpArr]

def makeResArray(tmpArr, k):
  return [el%2**k / 2**k for el in tmpArr]

def makeResBernulliArray(tmpArr, k, n):
  return [((el%2**(k+n) - el%(2**n)) >> n)/2**k for el in tmpArr]

def execute_formula(mode, formula, k, n):
  formula = make_formula_executable(formula)
  answer = {'x': [], 'y': []}

  print("Mode = ", mode)
  print("Formula = ", formula)  
  print("K = ", k)
  print("N = ", n)
  
  tmpX = makeArrayTmpX(mode, k, n)
  #print("tmpX", tmpX)
  xArray = makeXArray(tmpX, k)
  #print("xArray", xArray)

  yArray = []
  
  # if sync mode
  if (mode == 0):
    tmpY = makeArrayTmpY(tmpX, formula)
    yArray = makeResArray(tmpY, k)

  # if async mode
  if (mode == 1):
    pass

  # if Bernulli mode
  if (mode == 2):
    yArray = makeResBernulliArray(tmpX, k, n)

  #print("yArray", yArray)

  print("Done")
  print("")

  answer['x'] = xArray
  answer['y'] = yArray

  return answer