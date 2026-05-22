from ex0 import FlameFactory, AquaFactory
from ex1 import TransformCreatureFactory, HealingCreatureFactory
from ex2 import NormalStrategy, DefensiveStrategy, AggressiveStrategy


def battle(battlers : list[tuple]) -> None:
    for i in range(0, len(battlers)):
        for j in range(i + 1, len(battlers)):
            print("\n* Battle *")
            opp1 = battlers[i]
            opp2 = battlers[j]
            creature1 = opp1[0].create_base()
            creature2 = opp2[0].create_base()
            print(creature1.describe())
            print(" vs.")
            print(creature2.describe())
            print(" now fight!")
            try:
                opp1[1].act(creature1)
                opp2[1].act(creature2)
            except Exception as e:
                print(e)


if __name__ == "__main__":
    Flameling = FlameFactory()
    Aquabub = AquaFactory()
    Normal = NormalStrategy()
    Healing = HealingCreatureFactory()
    Defensive = DefensiveStrategy()
    Transform = TransformCreatureFactory()
    Aggressive = AggressiveStrategy()

    print(f"Tournament 0 (basic)")
    battlers = [(Flameling, Normal), (Healing, Defensive)]
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    print("*** Tournament ***")
    print(f"{len(battlers)} opponents involved")
    battle(battlers)

    battlers = [(Flameling, Aggressive), (Healing, Defensive)]
    print(f"\nTournament 1 (error)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    print("*** Tournament ***")
    print(f"{len(battlers)} opponents involved")
    battle(battlers)

    battlers = [(Aquabub, Normal), (Healing, Defensive), (Transform,Aggressive)]
    print(f"\nTournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    print("*** Tournament ***")
    print(f"{len(battlers)} opponents involved")
    battle(battlers)
