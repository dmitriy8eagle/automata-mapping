import math
import json
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

def makeAsyncArrayTmpY(tmpX, formula, bits):
  BERNOULLI_AUTOMATON = """
  {
    "s0": { "0": { "out": "", "goto": "s1"}, "1": { "out": "", "goto": "s1"}},
    "s1": { "0": { "out": "0", "goto": "s1"}, "1": { "out": "1", "goto": "s1"}}
  }
  """
  
  automaton = json.loads(formula)
  #print("automaton ", automaton)

  def asyncMap(val):
    state = "s0"
    res = ""
    #print("int Value", val)

    binaryVal = "{0:{fill}{bits}b}".format(val, fill='0', bits=bits)
    #print("binary Value ", binaryVal)

    for letter in binaryVal[::-1]:
      res += automaton[state][letter]["out"]
      state = automaton[state][letter]["goto"]

    #print("binary After shift ", res[::-1])
    #print("int After shift ", int(res[::-1], 2))

    return int(res[::-1], 2)


  tmpY = [asyncMap(x) for x in tmpX]

  return tmpY

def makeXArray(tmpArr, k):
  return [el%2**k / 2**k for el in tmpArr]

def makeResArray(tmpArr, k):
  return [el%2**k / 2**k for el in tmpArr]

def makeResBernoulliArray(tmpArr, k, n):
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
  if mode == 0:
    tmpY = makeArrayTmpY(tmpX, formula)
    yArray = makeResArray(tmpY, k)

  # if async mode
  if mode == 1:
    tmpY = makeAsyncArrayTmpY(tmpX, formula, k+n)
    yArray = makeResArray(tmpY, k)

  # if Bernoulli mode
  if mode == 2:
    yArray = makeResBernoulliArray(tmpX, k, n)

  #print("yArray", yArray)

  print("Done\n")

  answer['x'] = xArray
  answer['y'] = yArray

  return answer