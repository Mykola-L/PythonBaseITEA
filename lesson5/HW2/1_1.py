import shutil # Подключаем модуль
shutil.copyfile(r'/home/py/mouse.txt', r'/home/py/new-mouse.txt')
# Указанный путь не будет существовать
shutil.copyfile(r'/home/py/mouse.txt', r'/go/here/no.txt')
IOError: [Errno: 2] No such file or directory
'/go/here/no.txt'