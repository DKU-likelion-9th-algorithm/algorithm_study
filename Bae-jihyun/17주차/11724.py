'''
bfs를 실행하면 한 연결요소인 노드끼리만 방문된다.
즉, 연결요소를 다 순회한 후에도 방문하지 않은 노드가 있다면 다른 연결요소이다.

'''

import sys
from collections import deque
input = sys.stdin.readline


def bfs(x):
    q = deque([x])
    visited.add(x)
    while q:
        now = q.popleft()
        for node in graph[now]:
            if node not in visited:
                visited.add(node)
                q.append(node)


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = set()
result = 0    # 연결요소 개수

# 양방향 그래프 입력받기
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 연결요소마다 bfs 실행
for i in range(1, N+1):    # 모든 노드에 방문
    if i not in visited:   # 방문하지 않았다면 다른 연결요소이다.
        result += 1        # 연결요소 결과 + 1 해주고
        bfs(i)             # 방문하지 않은 노드를 출발지로 bfs 순회한다.

# 결과 출력
print(result)
