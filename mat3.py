import matplotlib.pyplot as plt

x = [1, 4, 6, 7]
y = [3, 5, 8, 10]

plt.scatter(x, y)

plt.xlabel("ось Х")
plt.ylabel("ось Y")
plt.title("Тестовая диаграмма рассеяния")

# С помощью диаграммы рассеяния мы можем увидеть скопления точек и “одиночные”
# точки в стороне — выброшенные, не типичные, аномальные.

plt.show()
