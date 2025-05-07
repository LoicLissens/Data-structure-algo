def solution(args):
    out = []
    a = b = args[0]

    for n in args[1:] + [None]:
        if n != b + 1:
            if b == a:
                out.append(str(a))
            elif b == a + 1:
                out.extend([str(a), str(b)])
            else:
                out.append(str(a) + "-" + str(b))
            a = n
        b = n

    return ",".join(out)

## or someone did it like this
def solution(arr):
    ranges = []
    begin = end = arr[0]
    for n in arr[1:] + [None]:
        if n != end + 1:
            ranges.append(
                str(begin)
                if begin == end
                else "{}{}{}".format(begin, "," if begin + 1 == end else "-", end)
            )
            begin = n
        end = n
    return ",".join(ranges)


