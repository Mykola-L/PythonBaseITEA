# n=input()
# sum=0
# for i in n:
#     sum+=int(i)
# print(sum)

def sum_digits_numbers(n):
    sum = 0
    for i in n:
        sum += int(i)  # sum = sum + int(i)
    print(sum)
    return sum


n = input('Введіть, будь-ласка, число ')
sum_digits_numbers(n)