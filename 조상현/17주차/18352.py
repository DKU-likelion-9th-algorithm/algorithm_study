# x부터 BFS를 시작해 k만큼 가서 도착하는 노드들을 오름차순 출력

import sys
from collections import deque

input = sys.stdin.readline

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

answer = []

queue = deque([[X]])
visited = set([])
depth = 0
# BFS, 단 depth가 k를 넘어가면 중지
while queue and depth <= K:
    nodes = queue.popleft()
    next_level_nodes = []
    for node in nodes:
        if node not in visited:
            visited.add(node)
            if depth == K:
                answer.append(node)
            else:
                next_level_nodes += graph[node]
    if next_level_nodes:
        queue += [next_level_nodes]
    depth += 1

# k만큼 가서 도착하는 도시들이 있으면 오름차순 후 출력, 없으면 -1 출력
if answer:
    answer.sort()
    for i in answer:
        print(i)
else:
    print(-1)


