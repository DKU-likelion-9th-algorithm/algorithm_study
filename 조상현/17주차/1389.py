import sys
from collections import deque
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    data = list(map(int, input().split()))
    graph[data[0]].append(data[1])
    graph[data[1]].append(data[0])

answer_sum = 5005
answer = 102
# start_node에서 각 노드까지 가는데 걸리는 깊이 저장할 배열
kevin = [0 for _ in range(N + 1)]
# 각 노드에서 다른 노드들까지 가는데 걸리는 깊이 = 케빈파이컨의 수이다 -> BFS로 계산
for start_node in range(1, N + 1):
    queue = deque([[start_node]])
    visited = set([])
    depth = 0

    while queue:
        nodes = queue.popleft()
        next_level_nodes = []
        for node in nodes:
            if node not in visited:
                # set자료형은 append가 아니라 add로 더한다
                visited.add(node)
                kevin[node] = depth
                next_level_nodes += graph[node]
        depth += 1
        if next_level_nodes:
            queue += [next_level_nodes]
    # 새로 구한 케빈 베이컨수의 합이 기존의 답보다 작다면 답 갱신
    if answer_sum > sum(kevin):
        answer_sum = sum(kevin)
        answer = start_node

print(answer)
    
# 시작점을 바꿔가며 각 시작노드별로 다른 모든 노드에 도달하기까지의 깊이를 계산하면 된다고 생각했다
# 처음엔 DFS로 할라고 했는데, 푸는 도중에 DFS로 처리할 경우 A에서 B로 갈 때 왔던 길을 다시 거쳐서 가는 경우를
# 배제하는 방법이 애매해서 BFS로 바꿔서 풀었다
# DFS, BFS 모두 그래프에서의 탐색방법으로 알고 있으나 방법의 차이만 알지 어떤 상황에서 쓰이는 건진 잘 몰랐는데
# 어떤 상황에선 뭘 쓰는게 좋을지를 한번쯤은 생각해보는게 좋을 것 같다는 힌트를 준 문제