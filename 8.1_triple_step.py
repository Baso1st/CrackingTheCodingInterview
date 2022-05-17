

def count_ways(n):
    memo = [0] * (n + 1)
    return count_ways_memoized(n, memo)

def count_ways_memoized(n, memo):
    if n < 0:
        return 0 
    if n == 0:
        return 1
    
    if memo[n] > 0:
        return memo[n]

    memo[n] = count_ways_memoized(n-1, memo) + count_ways_memoized(n-2, memo) + count_ways_memoized(n-3, memo)

    return memo[n]


def main():
    print(count_ways(500))


if __name__ == '__main__':
    main()