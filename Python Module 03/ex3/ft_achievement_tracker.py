import random

def gen_player_achievements():
    achievements = ['Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner', 
                    'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable', 
                    'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind', 'Boss Slayer']
    
    nbr_achievements = random.randint(0, len(achievements))
    chosen_achievements = set(random.sample(achievements, nbr_achievements))
    return (chosen_achievements)

if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    players = ["alice", "bob", "charlie", "dylan"]
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()
    players_print = [alice, bob, charlie, dylan]
    j = 0
    for i in players_print:
        print(f"Player {players[j].capitalize()}: {i}")
        j += 1
    print(f"\nAll distinct achievements: {alice | bob | charlie | dylan}")
    print(f"\nCommon achievements: {alice & bob & charlie & dylan}")
    print(f"\nOnly Alice has: {alice - bob - charlie - dylan}")
    print(f"Only Bob has: {bob - alice - charlie - dylan}")
    print(f"Only Charlie has: {charlie - bob - alice - dylan}")
    print(f"Only Dylan has: {dylan - charlie - bob - alice}")
    print(f"Alice is missing: {(alice | bob | charlie | dylan) - alice}")
    print(f"Bob is missing: {(alice | bob | charlie | dylan) - bob}")
    print(f"Charlie is missing: {(alice | bob | charlie | dylan) - charlie}")
    print(f"Dylan is missing: {(alice | bob | charlie | dylan) - dylan}")