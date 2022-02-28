'''
Для заданного числа найдите ближайший к нему элемент в векторе
Найдите N наибольших значений в векторе
'''

import numpy as np
#Создайте вектор с элементами от 12 до 42
x = np.arange(12, 24)
print (x)
#Создайте вектор из нулей длины 12, но его пятый елемент должен быть равен 1
print()
x = np.full((12,), 0) 
x[4] = 1
print (x)
#Создайте матрицу (3, 3), заполненую от 0 до 8
print ()
x = np.arange(0, 9).reshape((3,3))
print (x)
#Найдите все положительные числа в np.array([1,2,0,0,4,0])
print ()
a = np.array([1,2,0,0,4,0])
print(a[a > 0])  
#Умножьте матрицу размерности (5, 3) на (3, 2)
print ()
a = np.arange (0, 15).reshape (5, 3)
b = np.arange (0, 6).reshape (3, 2)
print (a.dot(b))
#Создайте матрицу (10, 10) так, чтобы на границе были 0, а внтури 1
print ()
x = np.ones((10, 10))
x[1:-1, 1:-1] = 0
print(x)
#Создайте рандомный вектор и отсортируйте его
x = np.random.random(10)
print("Original array:")
print(x)
x.sort()
print("Sorted array:")
print(x)
#Каков эквивалент функции enumerate для numpy массивов?
Z = np.arange(9).reshape(3,3)
for index, value in np.ndenumerate(Z):
    print(index, value)
for index in np.ndindex(Z.shape):
    print(index, Z[index])

