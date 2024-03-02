import heapq
import sys
input = sys.stdin.readline

hq = []
n = int(input())
for _ in range(n):
    x = int(input())
    if x == 0:
        if hq:
            print(heapq.heappop(hq)[1])
        else:
            print(0)
    else:
        heapq.heappush(hq, (abs(x), x))