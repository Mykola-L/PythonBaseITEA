y = 50 # глобальна змінна

def my_function():
    x = 10 # локальна змінна
    print(x)

def my_function_2():
    global y # глобальна змінна всередині функції
    # global y += 10 # такий запис робити не можна
    y += 10 # y = y + 10
    print(y)

print(y)
my_function_2()
print(y)
