# https://www.acmicpc.net/problem/2096
import sys

input = sys.stdin.readline

N = int(input())

'''
메모리 초과
num_list = []

for _ in range(N):
    num_list.append(list(map(int, input().split(" "))))


max_dp = [[0 for _ in range(3)] for _ in range(N)]  3XN
min_dp = [[0 for _ in range(3)] for _ in range(N)]

max_dp[0] = num_list[0]
min_dp[0] = num_list[0]

for i in range(1, N):
    max_dp[i][0] = max(max_dp[i-1][0], max_dp[i-1][1])+num_list[i][0]
    min_dp[i][0] = min(min_dp[i-1][0], min_dp[i-1][1])+num_list[i][0]

    max_dp[i][1] = max(max_dp[i-1][0], max_dp[i-1][1],
                       max_dp[i-1][2]) + num_list[i][1]
    min_dp[i][1] = min(min_dp[i-1][0], min_dp[i-1][1],
                       min_dp[i-1][2]) + num_list[i][1]

    max_dp[i][2] = max(max_dp[i-1][1], max_dp[i-1][2]) + num_list[i][2]
    min_dp[i][2] = min(min_dp[i-1][1], min_dp[i-1][2]) + num_list[i][2]

    #i번째에 영향 미치는 것은 i-1번째 밖에 없음
    
print(max(max_dp[N-1]), min(min_dp[N-1]))

--> 
슬라이딩 윈도우 기법:
메모이제이션을 할 때 더 이상 사용하지 않는 값을 저장하지 않고 배열을 계속하여 갱신해주는 것

'''
'''
0 0 0
0 0 0
'''


max_dp = [[0 for _ in range(3)] for _ in range(2)]
min_dp = [[0 for _ in range(3)] for _ in range(2)]

for i in range(N):
    a, b, c = map(int, input().split())

    max_dp[1][0] = max(max_dp[0][0], max_dp[0][1])+a
    min_dp[1][0] = min(min_dp[0][0], min_dp[0][1])+a

    max_dp[1][1] = max(max_dp[0][0], max_dp[0][1], max_dp[0][2])+b
    min_dp[1][1] = min(min_dp[0][0], min_dp[0][1], min_dp[0][2])+b

    max_dp[1][2] = max(max_dp[0][1], max_dp[0][2])+c
    min_dp[1][2] = min(min_dp[0][1], min_dp[0][2])+c

    max_dp[0][0], max_dp[0][1], max_dp[0][2] = max_dp[1][0], max_dp[1][1], max_dp[1][2]
    min_dp[0][0], min_dp[0][1], min_dp[0][2] = min_dp[1][0], min_dp[1][1], min_dp[1][2]

print(max(max_dp[1]), min(min_dp[1]))
