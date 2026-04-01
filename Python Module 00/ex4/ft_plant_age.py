def ft_plant_age():
    harvest = input("Enter plant age in days: ")
    if (int(harvest) > 60):
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
