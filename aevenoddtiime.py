n, e = map(int, input().split())

odd_count = (n + 1) // 2  

if e <= odd_count:
    print(2 * e - 1)
else:
    e_even = e - odd_count
    print(2 * e_even)