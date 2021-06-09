# Assuming that s1 and s2 will always bet positive integer, the main goal is to implement a function
# that take this number  add decomposite and add it to this same number (eg: 517 will be 5+1+7 + 516)
# untill find a commun number (join number) to these two numbers (they will always have one)


def Num(n):
    return sum([int(num) for num in str(n)]) + int(n)


def compute_join(s1, s2):
    n1, n2 = Num(s1), Num(s2)
    if n1 == n2:
        return n1
    else:
        return compute_join(n1, n2)
