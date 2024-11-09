# 2.Построй диаграмму рассеяния для двух наборов случайных данных, сгенерированных
# с помощью функции `numpy.random.rand`.
import numpy as np
import matplotlib.pyplot as plt

random_array1 = np.random.rand(5)  # массив из 5 случайных чисел
random_array2 = np.random.rand(5)  # массив из 5 случайных чисел

print(random_array1)
print(random_array2)

plt.scatter(random_array1, random_array2)

plt.xlabel("ось Х")
plt.ylabel("ось Y")
plt.title("Диаграмма рассеяния")

# С помощью диаграммы рассеяния мы можем увидеть скопления точек и “одиночные”
# точки в стороне — выброшенные, не типичные, аномальные.

plt.show()
