# 5! = 1*2*3*4*5 факторіал п'яти. Факторіал це множення всіх чисел підряд які є
PI = 3.1415

def factorial(n):
    num = 1

    while n >= 1:
        num = num * n
        n = n - 1
    return num
    #print(num)

result = factorial(5) # в змінну result зберігається результат роботи функції factorial() від 5
print(result)


# 1 = 1*5
# num = 5
# 5=5-1
# n=4
# return 5
#
# num = 5*4
# n = 4-1 = 3
# return 20
#
# num = 20*3 = 60
# n = 3-1 = 2
# return 60
#
# num = 60*2 = 120
# n = 2-1 = 1
# return 120
#
# num = 120*1 = 120
# n = 1-1 = 0
# return 120


