def count_bits(n):
    return bin(n).count("1") # Or return n.bit_count()

## The way I did it in go :
def countBits(n):
    total = 0
    while n > 0:
        total += n % 2
        n >>= 1
    return total
