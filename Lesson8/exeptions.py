# якщо користувач введе замість цифр букви або інші символи
try:
    number1 = float(input('Введіть ділене '))
    number2 = float(input('Введіть дільник '))
except ValueError: # блок Exception виконається, якщо виконається будь-який виняток який наслідується від Exception
    # Ієрархія винятків, презентація, урок 8, ст. 7

    print('Ви ввели невірні дані. Ваші дані замінені на 1')
    number1 = 1
    number2 = 1
    # або розпаковка кортежу, записи вверху і внизу ідентичні
    # number1, number2 = 1, 1


try: # відповідає за потенційно небезпечний код
    1 + '1'
    result = number1 / number2
except ZeroDivisionError:
    # відповідає за те, що має відбуватися у випадку винятку except
    result = number1 # якщо користувач ділить на 0, програма повертає ділене
except TypeError:
    result = number1
    print('Помилка типів!')

print(result)

