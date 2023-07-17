"""
Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним классы исключения с выводом подробной информации. 
Поднимайте исключения внутри основного кода.
"""

from math import pi

class InvalidRadiusTypeError(Exception):
    def __init__(self, message="Radius must be a non-negative real number only"):
        self.message = message
        super().__init__(self.message)


class NegativeRadiusError(Exception):
    def __init__(self, message="Radius can't be negative"):
        self.message = message
        super().__init__(self.message)


def circle_area(radius):
    if type(radius) not in [int, float]:
        raise InvalidRadiusTypeError()
    if radius < 0:
        raise NegativeRadiusError()
    return pi * radius ** 2

# Теперь при вызове функции circle_area() с некорректным радиусом будут выбрасываться соответствующие исключения:
try:
    area = circle_area(15)
except InvalidRadiusTypeError as e:
    print(e)  # Выводится сообщение об ошибке "Radius must be a non-negative real number only"
except NegativeRadiusError as e:
    print(e)  # Выводится сообщение об ошибке "Radius can't be negative"
