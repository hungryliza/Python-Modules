import random

if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    initial_lst = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    lst_cap = [i.capitalize() for i in initial_lst]
    only_cap = [i for i in initial_lst if i[0].isupper()]
    dic = {item: random.randint(0, 1000) for item in lst_cap}
    average = round(sum(dic.values()) / len(dic), 2)
    high_score = {key: dic[key] for key in dic.keys() if dic[key] > average}
    print(f"Initial list of players: {initial_lst}")
    print(f"New list with all names capitalized: {lst_cap}")
    print(f"New list of capitalized names only: {only_cap}")
    print(dic)
    print(f"Score average is {average}")
    print(f"High scores: {high_score}")