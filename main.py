import math
import cv2
import matplotlib.pyplot as plt

def main():
    way = "D:/Programiing/Python/Labs/4 Assignment_Part 2/Task.png"
    img = cv2.imread(way)
    cv2.imshow('Task4', img)
    cv2.waitKey(0)
    #cv2.destroyWindow('Task4')

    x = float(input('Enter x:'))
    a = float(input('Enter a:'))
    b = float(input('Enter b:'))
    c = float(input('Enter c:'))
    if x > a and b == 7:
        Z = a * x**3 + b * math.log(2 * x**2)
    elif x < a:
        Z = c * math.sqrt(abs(b + c * x**2 - a))
    else:
        Z = math.log10(2 * x + 3 * b**3)
    print(f'Z = {Z}')
    if Z > 153:
        print(f'Q = {2 * Z**2 + math.log(a)}')
    elif Z <= 153:
        print(f'Q = {2 * Z**2 + math.exp(x)}')
    input()
main()