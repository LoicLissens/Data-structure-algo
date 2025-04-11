def josephus(items,k):
    if not items:
        return []
    if k == 1:
        return items
    result = []
    index = 0
    while len(items) > 0:
        index = (index + k - 1) % len(items)
        result.append(items.pop(index))
    return result

# Golfed:
def josephus(xs, k):
    i, ys = 0, []
    while len(xs) > 0:
        i = (i + k - 1) % len(xs)
        ys.append(xs.pop(i))
    return ys