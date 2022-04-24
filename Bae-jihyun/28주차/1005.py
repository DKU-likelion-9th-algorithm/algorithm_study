import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    # 입력 받기
    n, k = map(int, input().split())
    cost = [0] + list(map(int, input().split()))  # 각 건물당 건설에 걸리는 시간
    graph = [[] for _ in range(n+1)]              # 건설 순서
    isStart = [0] * (n+1)               # 진입차수 구하기 = 출발지 찾기 (도착지마다 +1을 해줘서 isStart가 0인 곳이 출발지)
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)                        # a를 거쳐야 b로 갈 수 있다.
        isStart[b] += 1
    arrive = int(input())

    # 출발지 찾기
    dp = [0]*(n+1)    # dp : 출발지부터 index(현재 건물)까지 건설할 때 걸리는 시간
    q = deque()
    for i in range(1, n+1):
        if isStart[i] == 0:
            q.append(i)
            dp[i] = cost[i]
    # 출발지는 아니지만 진입차수가 0인 건물이 있기 때문에 break는 하지 않음.

    while q:
        index = q.popleft()
        for i in graph[index]:
            dp[i] = max(dp[index]+cost[i], dp[i])   # dp[index] : 이전 건물까지의 최대시간, cost[i] : 현재 건물 짓는 시간
            isStart[i] -= 1
            # 건물을 언제 다 짓고 다음 건물로 넘어가냐?
            if isStart[i] == 0:
                q.append(i)
                
    print(dp[arrive])

# 부끄러워 안 내