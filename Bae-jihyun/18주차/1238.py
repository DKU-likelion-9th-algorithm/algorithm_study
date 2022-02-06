'''
다익스트라 알고리즘은 한 정점에서 다른 여러 정점으로 가는 최소 거린를 구할 수 있다.
따라서 파티가 끝나고 각자 집으로 가는 길은 다익스트라를 사용하면 되지만,
그 반대로 여러 정점에서 한 정점으로 가는, 파티로 출발하는 최소 거리는 다익스트라 알고리즘으로 풀 수 없다.
그래서 그래프의 방향을 역방향으로 입력받은 rev_graph를 이용해 다익스트라 알고리즘을 적용했다.

ex)
1 -> 2(파티장소)의 가중치는 4, 2(파티장소) -> 1의 가중치는 1인 경우
파티장소에서 집으로 오는 최소 경로는 1로, 파티장소에서 (여러)집으로 가는 최소 경로를 구하는 다익스트라 알고리즘 사용가능
반대로 집에서 파티장소로 가는 최소 경로는 4로, 1 -> 2 가중치가 4인 그래프의 역방향 그래프인 2 -> 1 의 가중치는 4인 것을 이용해 다익스트라 알고리즘 사용가능
결국 2 -> 1은 한 정점(파티장소)에서 여러 정점(집)으로 가는 것이기 때문이다. 가중치의 값을 알고리즘에 맞게 바뀐 것 뿐.
'''


import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(graph, result, X):
    result[X] = 0  # 파티 장소는 최단 경로가 0
    q = []         # 최소 힙 (작은 인덱스를 가진 정점부터 차례대로 계산할 수 o)
    heapq.heappush(q, (result[X], result.index(result[X])))  # (최단 경로,해당 인덱스)

    while q:
        vertex, index = heapq.heappop(q)  # vertex = X부터의 최단 경로, index = 해당 인덱스

        if result[index] < vertex:  # 최단거리를 찾고 있기 때문에 현재까지의 최소 경로값이 큐값에서 나온 값보다 작으면 볼 필요없음
            continue

        for x, y in graph[index].items():  # x는 현재 정점과 인접한 또 다른 정점, y는 가중치
            weight = y + vertex   # 출발지부터 최소 vertex 가중치를 가진 index를 지나 x로 가는데 생성되는 가중치
            if result[x] >= weight:  # 갱신 시킨 weight가 여태까지보다 더 작은 값이면
                result[x] = weight   # result 갱신 시키기
                heapq.heappush(q, (result[x], x))  # (경로가중치, 인덱스)


N, M, X = map(int, input().split())
graph = {}      # 그래프를 표현한 딕셔너리
rev_graph = {}  # 역방향 그래프를 표현한 딕셔너리
result = [INF for _ in range(N+1)]      #정방향 그래프 다익스트라
rev_result = [INF for _ in range(N+1)]  #역방향 그래프 다익스트라

for i in range(1, N+1):
    graph[i] = {}
    rev_graph[i] = {}

for _ in range(M) :
    s, e, t = map(int, input().split())
    graph[s][e] = t
    rev_graph[e][s] = t

dijkstra(graph, result, X)          # 파티장소 -> 각 마을 최소 경로 탐색
dijkstra(rev_graph, rev_result, X)  # 역방향 그래프를 이용한  각 마을 -> 파티장소 최소 경로 탐색

# 오고 가는데 걸리는 시간 계산
for i in range(1, len(result)):
    result[i] += rev_result[i]

result[0] = 0  # [0]은 계산을 돕기 위해 사용하지 않음. MAX값을 구해줘야하는데 무의미한 값이기 때문에 0으로 처리
print(max(result))



'''
튜플(tuple)은 리스트와 거의 유사.
튜플 vs 리스트 
리스트는 [ ]으로 둘러싸지만 튜플은 ( )으로 둘러싼다.
리스트는 그 값의 생성, 삭제, 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다.

graph는 tuple, dict, set 다 사용가능

다익스트라 
한 정점에서 다른 여러 정점으로 이동하는 최소 경로
'''