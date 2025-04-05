def tower_builder(n_floors):
    list = []
    for i in range(n_floors):
        list.append(" " * (n_floors - i - 1) + "*" * (2 * i + 1)+" " * (n_floors - i - 1))
    return list
# Could be golfed with comprehension list
def tower_builder(n):
    return [" " * (n - i - 1) + "*" * (2*i + 1) + " " * (n - i - 1) for i in range(n)]