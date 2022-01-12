def createLineSpeed():
  x1 = []
  y1 = []
  x2 = []
  y2 = []
  print("Enter the beginning and ending of two line (0-1) (xb1,yb1,xe1,ye1,xb2,yb2,xe2,ye2)")
  Bp = input("Enter line position :").split(",")
  x1.append((Bp[0]))
  y1.append((Bp[1]))
  x1.append((Bp[2]))
  y1.append((Bp[3]))
  x2.append((Bp[4]))
  y2.append((Bp[5]))
  x2.append((Bp[6]))
  y2.append((Bp[7]))
  return x1,y1,x2,y2
