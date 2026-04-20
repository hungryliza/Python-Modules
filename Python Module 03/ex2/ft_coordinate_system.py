import math

def get_player_pos():
    while(True):
        try:
            player_in = input("Enter new coordinates as floats in format 'x,y,z':")
            x, y, z = player_in.split(",")
            return(float(x), float(y), float(z))
        except ValueError:
                print("Invalid syntax")

if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print(f"Get a first set of coordinates")
    tup = get_player_pos()
    print(f"Got a first tuple: {tup}")
    print(f"It includes: X={tup[0]}, Y={tup[1]}, Z={tup[2]}")
    print(f"Distance to center: {round(math.sqrt(tup[0]**2 + tup[1]**2 + tup[2]**2), 4)}")
    print(f"\nGet a second set of coordinates")
    tup1 = get_player_pos()
    print(f"Distance between the 2 sets of coordinates: "
          f"{round(math.sqrt((tup1[0]-tup[0])**2 +(tup1[1]-tup[1])**2 + (tup1[2]-tup[2])**2), 4)}")
