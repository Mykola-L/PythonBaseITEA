import random

def password_generator(a):
    length = a
    passwd = list('1234567890abcdABCD!@#$%^&*()-=_?qwertySDFGH')
    random.shuffle(passwd)
    passwd = ''.join([random.choice(passwd) for x in range(length)])
    print(passwd)

    my_file = open("PWTask2_2.txt", 'a')
    my_file.write(f'{passwd} \n')

    my_file.close()

    return passwd

password_generator(8)