from functions2 import factorial, PI # імпортуємо константу Pi
import functions2
r = functions2.factorial(10) # але після назви файлу (об'єкта), потрібно вказувати назву функції.
print(r)
r = factorial(10)
print(r)


print(PI) # 1 варіант
print(functions2.Pi) # 2 варіант. Назва файлу, через крапку назва змінної яку імпортую.