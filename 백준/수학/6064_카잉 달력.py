t = int(input())

for _ in range(t):
    m, n, x, y = map(int, input().split())
    k = x
    while k <= m * n:
        if (k - x) % m == 0 and (k - y) % n == 0:
            print(k)
            break
        k += m
    if k > m * n:
        print(-1)