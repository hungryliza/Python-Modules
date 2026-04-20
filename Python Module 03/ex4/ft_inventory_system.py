import sys

def display_inventory():
    if len(sys.argv) != 1:
        dic = {}
        for arg in sys.argv[1:]:
            splitted = arg.split(":")
            if (len(splitted) == 2):
                try:
                    if (splitted[0] not in dic):
                        dic.update({splitted[0] : int(splitted[1])})
                    else:
                        print(f"Redundant item '{splitted[0]}' - discarding")
                except ValueError as e:
                    print(f"Quantity error for {splitted[0]}: {e}")
            else:
                print(f"Error - invalid parameter: {arg}")
        val_lst = list(dic.values())
        max = val_lst[0]
        min = val_lst[0]
        for i in val_lst:
            if i > max:
                max = i
            continue
        for i in val_lst:
            if i < min:
                min = i
            continue
        print(f"Got inventory : {dic}")
        print(f"Item list : {list(dic.keys())}")
        print(f"Total quantity of the {len(dic)} items: {sum(dic.values())}")
        for item in list(dic.keys()):
            print(f"Item {item} represents {round(dic[item] / sum(dic.values()) * 100, 1)}%")
        for key in dic.keys():
            if dic[key] == max:
                print(f"Item most abundant: {key} with quantity {max}")
                break
        for key in dic.keys():
            if dic[key] == min:
                print(f"Item least abundant: {key} with quantity {min}")
                break
    else: 
        print("Your inventory is empty, please collect items")

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    display_inventory()