import sys
import heapq
input = sys.stdin.readline
INF = float(1e9)


def dijkstra(start):
    dist[start] = 0  # 출발 도시는 최단 경로 0
    visited = []
    q = []         # 최소 힙 (작은 인덱스를 가진 정점부터 차례대로 계산할 수 o)
    heapq.heappush(q, (0, start))  # start 인덱스부터 시작하기 위해 heap에 넣기

    while q:
        edge, node = heapq.heappop(q)  # edge = X부터의 최소 비용, node = 해당 도시 번호

        #if edge > dist[node]:      이 조건 또는 아래 방문 체크 둘 중 하나 꼭 해줘야함
        #    continue
        if node in visited:
             continue
        visited.append(node)

        for nextnode, nextcost in graph[node]:  # nextcost는 비용, nextnode는 현재 도시와 인접한 다른 도시
            if dist[node] + nextcost < dist[nextnode]:
                dist[nextnode] = dist[node] + nextcost
                heapq.heappush(q, (dist[nextnode], nextnode))


n = int(input())
m = int(input())
graph = [[]for _ in range(n+1)]
dist = [INF for _ in range(n+1)]

# graph 입력받기
for _ in range(m):
    s, e, v = map(int, input().split())
    graph[s].append([e, v])

sc, ec = map(int, input().split())  # 출발도시, 도착도시 정해짐
dijkstra(sc)
print(dist[ec])
'''
다익스트라 알고리즘
간선마다 비용이 다르거나 한 정점에서 여러 정점으로 갈 때(한 정점에서 한 정점으로 가는 최소비용도 가능) 사용

'''