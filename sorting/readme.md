Sorting a list can be done in multiple ways (in order of efficiency, ascending):

## Brute Force
*Complexity*:
If the list has length `n`, for each possibility: `n` computations => `n(n-1)(n-2)...1 = n! (n factorial) possibilities`.
This means it has a complexity of `O(n * n!)`.

## Bubble Sort
Iterate over a pair of elements `n` and `n + 1` and swap them only if `n + 1` is smaller than `n`.
The iteration continues until it reaches the end of the list. If a swap has been made during the iteration, we start over; if not, the list is sorted.

*Complexity*:
- `n` operations per swap
- In the worst case, we have `n` swaps
- `O(n * n)`
- So i n = 100 => complexity is 10 000

## Merge Sort
The list is split into two halves, each half is sorted, and then merged together.
To sort a half, this method is applied recursively until `n` (the size of the list) is equal to 1.
- `n`operation per level in the tree
- `log(n)` level so the complexity is `O(n*log(n))`
-   So i n = 100 => complexity is 664

[Ressource](https://www.youtube.com/watch?v=FIwcgikJWUc&list=PLOapGKeH_KhFtAo_-qEA98bAJwTHGus1X&index=10)