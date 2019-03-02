from effective_python.models.inheritances import Animal
from effective_python.module.models import Model


class Dog(Model, Animal):
    _name = 'animal.dog'
    enemy_name = 'animal.shark'
    speech = 'Woof'


class Cat(Model, Animal):
    _name = 'animal.cat'
    enemy_name = 'animal.dog'
    speech = 'Mew'


class Bird(Model, Animal):
    _name = 'animal.bird'
    enemy_name = 'animal.cat'
    speech = 'Twink'


class Shark(Model, Animal):
    _name = 'animal.shark'
    enemy_name = 'animal.bird'
    speech = 'Rrrra'
