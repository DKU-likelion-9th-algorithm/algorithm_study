# 저번 학기 자료구조 시간에 관련된 과제를 한 적이 있어서 쉽게 접근함
# DFS / BFS는 연결된 모든 노드를 방문하기 때문에, 전체적으로 볼 때 DFS / BFS를 수행한 횟수가
# 연결 요소의 개수와 같다

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = set([])
answer = 0

def bfs(start_node):
    queue = deque([start_node])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            queue += graph[node]
# 모든 노드에 대해 순회하며 방문한 적 없으면 그 노드를 시작점으로 bfs
for node in range(1, N + 1):
    if node not in visited:
        answer += 1
        bfs(node)

print(answer)
