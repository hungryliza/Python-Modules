import random
import typing

def gen_event() -> typing.Generator[tuple, None, None]:
    names = ["Alice", "Bob", "Dylan", "Charlie"]
    actions = ["run", "eat", "sleep", "grab", "move", "release", "climb", "swim", "move"]
    while (True):
        ran_names = random.choice(names)
        ran_actions = random.choice(actions)
        yield (ran_names, ran_actions)

def consume_event(lst_ten):
    while(lst_ten):
        to_remove = random.choice(lst_ten)
        lst_ten.remove(to_remove)
        yield to_remove

if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    generator = gen_event()
    for i in range(1000):
        name, action = next(generator)
        print(f"Event {i}: Player {name} did action {action}")
    lst_ten = [next(generator) for i in range(10)]
    print(f"Built list of 10 events: {lst_ten}")
    for event in consume_event(lst_ten):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {lst_ten}")