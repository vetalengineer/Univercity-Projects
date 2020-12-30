import math
import matplotlib.pyplot as plt
import cv2

# Ревуцкий Виталий ФО21
# Вариант 8

def main():
 way = "D:/Programiing/Python/Labs/IDZ/idzTask.png"
 img = cv2.imread(way)
 cv2.imshow('Task', img)
 #cv2.waitKey(5000)
 #cv2.destroyWindow('Task')

 #Part 1 "Построить график функции с заданным шагом табуляции"
 #==========================================================================================================

 xList = []
 yList = []

 x = -10

 with open("Data.txt", "w") as dataFile:
  with open("Data.txt", "a") as dataFile:
   print('\n FUNCTION TABULATION \n#==========================================================================================================\n')
   dataFile.write("\n FUNCTION TABULATION\n#==========================================================================================================\n")

  while x <= 10:
   y = math.acos((1 - x**2)/(1 + x**2))
   xList.append(x)
   yList.append(y)
   x += 0.2
   print(f"y = {round(y, 2)}, x = {round(x, 2)}")

   with open("Data.txt", "a") as dataFile:
    dataFile.write(f"y = {round(y, 2)}, x = {round(x, 2)}\n")

 plt.figure(figsize = (8, 5))
 plt.grid(which="major", linewidth=1.2)
 plt.xlabel("x", fontsize=14)
 plt.ylabel("y", fontsize=14)
 plt.tick_params(which='major', length=10, width=1)
 plt.tick_params(which='minor', length=5, width=0.5)

 plt.plot(xList, yList, linestyle = 'dotted')
 #plt.show(block=False)
 plt.pause(1)

 # Part 2 "Сумма ряда"
 #==============================================================================================

 with open("Data.txt", "a") as dataFile:

  print('\n ROW SUM \n#==========================================================================================================\n')
  dataFile.write("\n ROW SUM\n#==========================================================================================================\n")

  x = float(input('Enter x: '))
  dataFile.write(f"\nx = {x}\n")
  try:
   a = float(input('Enter a: '))
   dataFile.write(f"a = {a}\n")

   b = float(input('Enter b: '))
   dataFile.write(f"b = {b}\n")

   E = 0
   print(f"E = {E}")
   dataFile.write(f"E = {E}\n")

   sum = float((a + x)/(b*x**2))
   n = 1
   k = 1
   i = 2
   func = ((2**n * x**k))  * (-1)**(n-1)  / (i * x**n + n*b)

   while float(abs(func)) > float(E):
    sum += float(func)
    n += 1
    k += 2
    i = i*n
    func = ((2**n * x**k)) * (-1)**(n-1) / (i * x**n + n * b)
    dataFile.write(f"\nRow sum = {sum}\n")
   print(f'\nRow sum = {sum}')
  except:
   print('\n>>>>>Uncorrect x, it must be x > 1 <<<<<')
 input()
 dataFile.close()
main()
