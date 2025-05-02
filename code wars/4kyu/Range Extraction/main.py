def solution(args):
    out = []
    beg = end = args[0]

    for n in args[1:] + [""]:
        if n != end + 1:
            if end == beg:
                out.append(str(beg))
            elif end == beg + 1:
                out.extend([str(beg), str(end)])
            else:
                out.append(str(beg) + "-" + str(end))
            beg = n
        end = n

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


