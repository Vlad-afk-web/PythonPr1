import math
#1
var_int = 10

var_float  = 8.4

var_str = 'No'

print("Завдання 1 " , var_int , var_float , var_str)
#2

big_int  = var_int * 3.5


print("Завдання 2 " , big_int)
#3

var_float -= 1

print("Завдання 3 " , var_float)
#4

var_int /= var_float

big_int /= var_float

print("Завдання 4 " , var_int , big_int)

#5

var_yes = 'Yes'
var_str = var_str + var_str + var_yes * 3

print("Завдання 5 " + var_str)

#6

a = int(input("Введіть число а: "))
b = int(input("Введіть число b: "))
c = int(input("Введіть число c: "))
x = int(input("Введіть число x: "))

y = math.sqrt(x ** 3 + a * x ** 2 + b * x + c)

print ("Введені вами числа: " , a , b , c , x)

print ("Резльтат функції 6 " , y)
