# https://www.acmicpc.net/problem/1956

import sys
input = sys.stdin.readline

V, E = map(int, input().split())

max = 10000*V + 1   # 전체 사이클 돌 경우 값(최대 거리:10000 * V) + 1

distance_list = [[max for _ in range(V+1)] for _ in range(V+1)]

for _ in range(E):
    start, end, distance = map(int, sys.stdin.readline().split())
    distance_list[start][end] = distance

# 플로이드-워셜 알고리즘
for i in range(1, V+1):
    for j in range(1, V+1):
        for k in range(1, V+1):
            distance_list[j][k] = min(
                distance_list[j][k], distance_list[j][i]+distance_list[i][k])

min_cycle = max
for i in range(1, V+1):
    min_cycle = min(min_cycle, distance_list[i][i])  # 자기 자신한테 돌아와야 되니까

if min_cycle == max:
    print(-1)
else:
    print(min_cycle)


'''
3 4
1 2 1
3 2 1
1 3 5
2 3 2

  0 1 2 3             0 1 2 3
0 X X X X           0 X X X X
1 X X 1 5    -->    1 X X 1 3(1.2 + 2.3)
2 X X X 2           2 X X 3 2
3 X X 1 X           3 X X 1 3(3.2 + 2.3)

'''
