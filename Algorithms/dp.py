def ways(sum, ar, memo):
    if sum in memo.keys():
        return memo[sum]

    if sum == 1:
        return 1
    if sum < 1:
        return 0
    total = 0
    for i in ar:
        total = total + ways(sum - i, ar, memo)
        memo[sum] = total
    return total


n = 40

ar = [2, 5, 3, 6]
memo = {}
print(ways(n, ar, memo))
