def power_sum(x, n, num=1):
    if x == 0:
        return 1
    if x < 0:
        return 0
    if num ** n > x:
        return 0
    take = power_sum(x - num**n, n, num + 1)
    skip = power_sum(x, n, num + 1)
    return take + skip
print(power_sum(100, 2, num=1))