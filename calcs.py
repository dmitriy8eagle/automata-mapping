import math
import numpy as np

def make_formula_executable(formula):
  COMMANDS = [ 'pow', 'sqrt', 'cos', 'sin', 'tag', 'log', 'pi' ]
  PREFIX = 'math.'

  for command in COMMANDS:
    formula = formula.replace(command, PREFIX+command)

  return formula

def execute_formula(formula, k):
  formula = make_formula_executable(formula)
  answer = {'x': [], 'y': []}
  #answer = eval(formula)
  answer['x'] = np.random.uniform(low=0, high=1, size=(10000,))
  answer['y'] = np.random.uniform(low=0, high=1, size=(10000,))
  return answer