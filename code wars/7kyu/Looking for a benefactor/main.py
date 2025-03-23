import math

# Taking the equation :  (sum + x) / (len + 1) = navg
# then x should be equal to (navg * (len + 1)) - sum

def new_avg(arr, newavg):
    if  newavg * (len(arr) + 1) > sum(arr):
        return math.ceil(newavg * (len(arr) + 1) - sum(arr))
    raise Error("Error expected")