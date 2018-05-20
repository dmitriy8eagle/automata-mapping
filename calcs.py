import math
import numpy as np

def make_formula_executable(formula):
  COMMANDS = [ 'pow', 'sqrt']
  BOOLEAN = {'OR': '|', 'XOR': '^', 'AND': '&'}
  PREFIX = 'math.'

  for command in COMMANDS:
    formula = formula.replace(command, command)

  for key, value in BOOLEAN.items():
    formula = formula.replace(key, value)

  formula = formula.replace('x', 'int(x)')
  print(formula)

  return formula

def makeArrayTmpX(k):
  return [int(x) for x in range(2**k)]

def makeArrayTmpY(tmpX, formula):
  return [eval(formula) for x in tmpX]

def makeXArray(tmpArr, k):
  return [el%2**k / 2**k for el in tmpArr]

def makeResArray(tmpArr, k):
  return [el%2**k / 2**k for el in tmpArr]

def makeResBernulliArray(tmpArr, k):
  return [((el%2**(k+1) - el%2**1) >> 2)/2**k for el in tmpArr]

def execute_formula(formula, k):
  formula = make_formula_executable(formula)
  answer = {'x': [], 'y': []}

  tmpX = makeArrayTmpX(k)
  print("tmpX", tmpX)
  xArray = makeXArray(tmpX, k)
  print("xArray", xArray)

  tmpY = makeArrayTmpY(tmpX, formula)
  yArray = makeResArray(tmpY, k)
  # yArray = makeResBernulliArray(tmpX, k)
  print("yArray", yArray)

  answer['x'] = xArray
  answer['y'] = yArray

  return answer