import sys


answer = 0
N = int(sys.stdin.readline())
buildings = list(int(sys.stdin.readline().rstrip()) for _ in range(N))





# # 당근 시간 초과
# import sys


# answer = 0
# N = int(sys.stdin.readline())
# buildings = list(sys.stdin.readline().rstrip() for _ in range(N))

# for i in range(N - 1):
#     buildings[i]
#     for j in range(i + 1, N):
#         if buildings[i] > buildings[j]:
#             answer += 1
#         else:
#             break

# print(answer)