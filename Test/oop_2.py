# 2) создай абстрактный класс Animal с абстрактным методом make_sound. Затем создай два дочерних класса:
# - Cat, который переопределяет метод make_sound, чтобы выводить "Мяу".
# - Dog, который переопределяет метод make_sound, чтобы выводить "Гав".
#
# Потом создай список животных и с помощью полиморфизма вызови метод make_sound для каждого из них.

'''Импортирую модуль для создания абстрактного класса'''
import abc

class Animal(abc.ABC):

    '''Чтобы определить абстрактный метод, нужно использовать аннотацию'''
    @abc.abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):

    def make_sound(self):
        print('Мяу!')

class Dog(Animal):

    def make_sound(self):
        print('Гав!')

cat = Cat()
dog = Dog()

for i in (cat, dog):
    i.make_sound()
