# рограма копіює 11 рядок, переносить нижче і вставляє
import pyautogui

pyautogui.FAILSAFE = False # ігноруємо винятки exception
# lesson3_coordinares = (93, 137)
# pyautogui.moveTo(lesson3_coordinares[0], lesson3_coordinares[1], 1) # 1 одна секунда


# Переместить мышку относительно текущего местоположения
# pyautogui.moveRel(-100, 100, 3) # виділяю 11 рядок

pyautogui.moveTo(1112, 178, 3)
pyautogui.dragRel(xOffset=-265, duration=3) # виділяє 11 рядок на 400 пікселів
pyautogui.hotkey('ctrl', 'c') # копіюю 11 рядок
pyautogui.moveRel(yOffset=350, xOffset=20, duration=2) # перемістимо курсор на 350 вниз по у, за 2 секунди
pyautogui.click() # клікаємо лівою кнопкою мишки
pyautogui.hotkey('ctrl', 'v') # вставляю 11 рядок



