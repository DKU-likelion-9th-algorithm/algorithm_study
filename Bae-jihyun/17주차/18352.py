import sys
from collections import deque
input = sys.stdin.readline


def bfs(x):
    q = deque([x])
    visited = set([x])
    while q:
        now = q.popleft()
        for node in graph[now]:
            if node not in visited:
                visited.add(node)
                result[node] = result[now]+1   # 목적지는 출발지에서 목적지까지 가는 각 전 단계 + 1
                if result[node] > K:   # 원하는 거리인 K보다 거리가 멀다면 더 깊게 들어갈 필요가 없다.
                    continue
                q.append(node)
    return result  # 출발지에서 각 노드로 도착하는 거리


N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]  # 입력 받을 그래프
result = [0]*(N+1)  # x가 도착해야 할 목적지(result의 인덱스 번호)까지의 거리가 담김.
# result를 dict로 만들 수 있을까요..? N+1사이즈, index를 키로 하는 dict를 생성하는 방법이 있을까요...?
flag = False        # result 안에 K가 있음을 나타내는 표시

# 단방향 그래프 입력받기
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

bfs(X)

# 결과 출력
for i in range(N+1):
    if result[i] == K:
        print(i)
        flag = True
if not flag:
    print(-1)


'''
bfs를 이용할 경우, 한번 방문한 노드를 다시 방문하면 거리가 늘어날 수 밖에 없다.
하지만 우리는 최단거리를 구하기 때문에 가장 짧게 방문하기만 하면 된다.
visited를 사용하면 다시 방문하여 거리가 늘어나는 것을 막을 수 있다. 

그래프에서 간선비용이 모두 동일할 때는 BFS 를 이용하여 최단 거리를 찾을 수 있다.
다익스트라의 경우는 간선비용이 다를 때 같을 때 모두 사용할 수 있다.
'''
