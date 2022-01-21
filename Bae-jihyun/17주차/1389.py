'''
1부터 N까지 돌아가며 각각 노드에서 출발해 모든 노드에 도착해야한다.
15주차 9372번과 유사하다고 느낌
'''


import sys
from collections import deque
input = sys.stdin.readline


def bfs(graph, x):
    ans = [0]*(N+1)  # ans의 인덱스 번호 = x가 도착해야 할 목적지
    q = deque([x])
    visited = set([x])
    while q:
        now = q.popleft()
        for i in graph[now]:
            if i not in visited:
                ans[i] = ans[now]+1   # 목적지는 출발지에서 목적지까지 가는 각 전 단계 + 1
                visited.add(i)
                q.append(i)
    return sum(ans)  # 출발지에서 각 노드로 도착하는 단계의 최종 합


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]   # 입력 받을 그래프
result = []  # 결과 담을 리스트

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 출발지마다 bfs 실행
for i in range(1, N+1):
    result.append(bfs(graph, i))

print(result.index(min(result))+1)
