# random випадковий, не називайте файл random, random це ім'я, вбудований модуль
# example приклад

import random # імпортуємо модуль random

a = [1, 100, 3]

my_random = random.randint(50, 100) # генерує випадкові числа від 50 до 100
print(my_random)

random_number = random.choice(a)
print(random_number)
