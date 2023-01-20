import sys

sys.setrecursionlimit(10 ** 9)


def dfs(node):
    visited[node] = True
    graph[node][0] = 0          # 얼리가 아닌 경우
    graph[node][1] = 1          # 얼리인 경우

    for t in tree[node]:        # 서브 트리 방문하며 얼리인 경우와 얼리가 아닌경우를 나눠 경우의 수 계산
        if visited[t]:
            continue
        dfs(t)

        graph[node][0] += graph[t][1]

        # 현재 노드가 얼리 어답터인 경우, 연결된 친구들은 얼리 어답터이거나 아니어도 됨.
        # 즉, 얼리 어답터인 친구(자식)와 아닌 친구(자식) 중 최소인 경우를 더해줌.
        graph[node][1] += min(graph[t][0], graph[t][1])
        # print(node, t, graph)


# 입력받기
N = int(sys.stdin.readline())
tree = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)

graph = [[0, 0] for _ in range(N + 1)]


# 실행
dfs(1)

# print(tree)
print(min(graph[1][0], graph[1][1]))


'''
서브트리로 계속 내려가야하기 때문에 bfs보다는 dfs사용

현재 노드가 얼리가 아닌 경우, 연결된 친구들은 모두 얼리 어답터여야 함. 즉, 연결된 친구(자식)들이 얼리인 경우를 더해줌.
graph[node][0] += graph[friend][1];

현재 노드가 얼리인 경우, 얼리인 자식과 아닌 자식 중 최소를 더함.
graph[node][1] += Math.min(graph[friend][0], graph[friend][1]);

주석해놓은 print의 주석을 풀면 계산과정 쉽게 확인가능
'''

"""
피드백 코멘트 :
트리 DP를 경험해보지 않으셨다면 어렵게 느낄 수 있는 문제인데 잘 풀어주셨네요.
고생하셨습니다!
"""
