class Animal:
    enemy_name = ''
    speech = 'Hello'

    def __init__(self):
        self.enemy = self.env[self.enemy_name]

    @classmethod
    def say(cls):
        print(cls.speech)

    def get_scared(self):
        print("My enemy talks like: ", end='')
        self.enemy.say()


class Transport:
    possible_passengers_names = []

    def __init__(self):
        self.possible_passengers = [self.env[p_name] for p_name in self.possible_passengers_names]

    def view_inside(self):
        print('My passenger talks like: ')
        for passenger in self.possible_passengers:
            passenger.say()
