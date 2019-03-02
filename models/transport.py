from effective_python.models.inheritances import Transport
from effective_python.module.models import Model


class Car(Model, Transport):
    _name = 'transport.car'
    possible_passengers_names = ['animal.cat', 'animal.bird', 'animal.dog']


class Bus(Model, Transport):
    _name = 'transport.bus'
    possible_passengers_names = ['animal.cat', 'animal.bird', 'animal.dog']


class Train(Model, Transport):
    _name = 'transport.train'
    possible_passengers_names = ['animal.cat', 'animal.bird', 'animal.dog', 'animal.shark']


class Plane(Model, Transport):
    _name = 'transport.plane'
    possible_passengers_names = []
