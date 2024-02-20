def fibonacci_memoized(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n]= fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
    return memo[n]

fibonacci_memoized(50)