from ex0.classesFactory import CreatureFactory
from .classes import Bloomelle, Shiftling, Sproutling, Morphagon


class HealingCreatureFactory(CreatureFactory):
    def create_base(self):
        return Sproutling()

    def create_evolved(self):
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self):
        return Shiftling()

    def create_evolved(self):
        return Morphagon()
