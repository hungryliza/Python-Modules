from abc import ABC, abstractmethod
from ex0.classes import Creature
from ex1.classes import TransformCapability, HealCapability


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature):
        ...

    @abstractmethod
    def is_valid(self, creature):
        ...


class NormalStrategy(BattleStrategy):
    def act(self, creature):
        print(creature.attack())

    def is_valid(self, creature):
        return True


class AggressiveStrategy(BattleStrategy):
    def act(self, creature):
        if self.is_valid(creature) is True:
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())
        else:
            raise Exception(f"Battle error, aborting tournament: "
                f"Invalid Creature '{creature.name}' "
                f"for this aggressive strategy")

    def is_valid(self, creature):
        return isinstance(creature, TransformCapability)


class DefensiveStrategy(BattleStrategy):
    def act(self, creature):
        if self.is_valid(creature) is True:
            print(creature.attack())
            print(creature.heal())
        else:
            raise Exception(f"Battle error, aborting tournament: "
                    f"Invalid Creature '{creature.name}' "
                    f"for this defensive strategy")

    def is_valid(self, creature):
        return isinstance(creature, HealCapability)
