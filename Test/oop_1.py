# 1) создай класс Transport, который будет содержать следующие атрибуты:
# brand (строка),
# model (строка),
# year (целое число).
#
# добавь метод get_info, который будет возвращать строку с информацией о транспортном средстве в формате:
# Brand: <brand>, Model: <model>, Year: <year>
#
# Далее создай два дочерних класса:
# Car, который будет добавлять атрибут transmission_type (строка) и метод get_info(переопределить метод родительского класса, добавив информацию о трансмиссии).
#
# Motorcycle, который будет добавлять атрибут engine_volume (целое число) и метод get_info(переопределить метод родительского класса, добавив информацию о двигателе).

class Transport:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")


class Car(Transport):

    def __init__(self, brand, model, year, transmission_type = 'Automatic'):
        super().__init__(brand, model, year)
        self.transmission_type = transmission_type

    def get_info(self):
        print(f'Brand: {self.brand}, Model: {self.model}, Year: {self.year}\nTransmission Type: {self.transmission_type}')

class Motorcycle(Transport):

    def __init__(self, brand, model, year, engine_volume):
        super().__init__(brand, model, year)
        self.engine_volume = engine_volume

    def get_info(self):
        print(f'Brand: {self.brand}, Model: {self.model}, Year: {self.year}\nEngine volume: {self.engine_volume}')


car = Car('BMW', 'X5', 2021, 'Handed')
motor = Motorcycle(car.brand, car.model, car.year, 2000)
car.get_info()
motor.get_info()