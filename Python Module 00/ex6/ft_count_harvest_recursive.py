def ft_count_harvest_helper(i, tot_days):
    if (i > tot_days):
        print("Harvest time!")
    else:
        print("Day", i)
        ft_count_harvest_helper(i + 1, tot_days)

def ft_count_harvest_recursive():
    tot_days = int(input("Days until harvest: "))
    ft_count_harvest_helper(1, tot_days)
