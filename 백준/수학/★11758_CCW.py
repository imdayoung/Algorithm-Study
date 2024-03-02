import sys
input = sys.stdin.readline

def ccw(x1, y1, x2, y2, x3, y3):
    temp = (x1 * y2 + x2 * y3 + x3 * y1) - (y1 * x2 + y2 * x3 + y3 * x1)

    if temp > 0:
        return 1
    elif temp < 0:
        return -1
    else:
        return 0


x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
print(ccw(x1, y1, x2, y2, x3, y3))