class Tomato:
    states = {0: 'не спелый',
              1: 'начал созревать',
              2: 'уже почти',
              3: 'созрел'
              }
    def __init__(self, _index, _state):
        self._index = _index
        self._state = 0

    def grow(self):
        if self._state<3:
            self._state += 1
        print(f'Tomato {self._index} is {Tomato.states[self._state]}')

    def is_ripe(self):
        if self._state == 3:
            return True
        else:
            return False

class TomatoBush:
    def __init__(self, num):
        self.tomatoes = [Tomato(i) for i in range(0, num)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def giva_away_all(self):
        self.tomatoes = []

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print('Садовник работает')
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Урожай собран')
        else:
            print('Урожай не созрел')

    @staticmethod
    def knowledge_base():
        print('Справка по садоводству!')

Gardener.knowledge_base()
tomatobush = TomatoBush(6)
gardener = Gardener('Leon', tomatobush)
gardener.work()
gardener.harvest()
gardener.work()
gardener.work()
gardener.harvest()