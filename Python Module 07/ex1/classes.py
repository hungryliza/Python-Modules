from abc import ABC, abstractmethod
from ex0.classesFactory import CreatureFactory
from ex0.classes import Creature

class HealCapability(ABC):
    @abstractmethod
    def heal(self, target):
        ...


class TransformCapability(ABC):
    @abstractmethod
    def transform(self):
        ...

    @abstractmethod
    def revert(self):
        ...


class Sproutling(Creature, HealCapability):
    def __init__(self):
        super().__init__("Sproutling", "Grass")

    def attack(self):
        return f"{self.name} uses Vine Whip!"

    def heal(self):
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self):
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self):
        return f"{self.name} uses Petal Dance!"

    def heal(self):
        return f"{self.name} heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Shiftling", "Normal")
        self.transformed = False

    def attack(self):
        if self.transformed is False:
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} performs a boosted strike!"

    def transform(self):
        self.transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self):
        self.transformed = False
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Morphagon", "Normal/Dragon")
        self.transformed = False

    def attack(self):
        if self.transformed is False:
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} unleashes a devastating morph strike!"

    def transform(self):
        self.transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self):
        self.transformed = False
        return f"{self.name} stabilizes its form."
