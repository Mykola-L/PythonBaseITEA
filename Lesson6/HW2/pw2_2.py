import random

def password_generator(a):
    length = a
    passwd = list('1234567890abcdABCD!@#$%^&*()-=_?жзиклпшщя')
    random.shuffle(passwd)
    passwd = ''.join([random.choice(passwd) for x in range(length)])
    print(passwd)  # шкиd69#&

    return passwd

password_generator(8)

