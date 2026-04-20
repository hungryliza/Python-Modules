def ft_count_harvest_helper(i: int, tot_days: int) -> None:
    if (i > tot_days):
        print("Harvest time!")
    else:
        print("Day", i)
        ft_count_harvest_helper(i + 1, tot_days)


def ft_count_harvest_recursive() -> None:
    tot_days = int(input("Days until harvest: "))
    ft_count_harvest_helper(1, tot_days)
