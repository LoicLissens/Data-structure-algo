def last_digit(n1, n2):
    n1 = int(n1)
    n2 = int(n2)

    if n1 == 0 and n2 == 0:
        return 1
    if n2 == 0:
        return 1
    if n1 == 0:
        return 0

    if n2 % 4 == 0:
        res = 4
    else:
        res = n2 % 4

    return  pow(n1, res) % 10

# Can be golfed as:
def last_digit(n1, n2):
    return pow( n1, n2, 10 )