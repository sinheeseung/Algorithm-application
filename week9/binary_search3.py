def arrangeCoins(n):
    left, right = 0,n
    while left <= right:
        k = (right + left) // 2
        current = k * (k + 1) // 2
        if current == n:
            return k
        if n <= current:
            right = k - 1
        else:
            left = k + 1
    return right

n = 8

answer = arrangeCoins(n)
print(answer)
