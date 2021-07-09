import numpy as np

def And(x1:int,x2:int) -> int:
  x = np.array([x1,x2])
  w = np.array([0.5,0.5])
  b = -0.7
  if np.sum(w * x) + b <= 0:
    return 0
  else:
    return 1
def Or(x1:int,x2:int) -> int:
  x = np.array([x1,x2])
  w = np.array([1,1])
  b = -0.5
  if np.sum(w * x) + b <= 0:
    return 0
  else:
    return 1

def Nand(x1:int,x2:int) -> int:
  x = np.array([x1,x2])
  w = np.array([-0.5,-0.5])
  b = 0.7
  if np.sum(w * x) + b <= 0:
    return 0
  else:
    return 1

def Xor(x1:int,x2:int) -> int:
  s1 = Nand(x1,x2)
  s2 = Or(x1,x2)
  y = And(s1,s2)
  return y

if __name__ == "__main__":
  print(Xor(0,0))
  print(Xor(0,1))
  print(Xor(1,0))
  print(Xor(1,1))

