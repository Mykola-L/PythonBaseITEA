import os
import sys
print(f'Операційна система {os.name}')
print(os.environ)
print(f'Кількість ядер {os.cpu_count()}')
print(f'Платформа {sys.platform}')