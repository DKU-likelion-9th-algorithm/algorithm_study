from collections import deque


def dfs(n):
    visited.append(n)
    print(n, end=" ")

    for v in lst[n]:
        if v in visited:
            continue
        dfs(v)


def bfs(n):
    q = deque([n])

    while q:
        v = q.popleft()
        if v in visited:
            continue
        print(v, end=" ")
        visited.append(v)
        for i in lst[v]:
            q.append(i)

n, m, v = map(int, input().split())
lst = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
    lst[a].sort()
    lst[b].sort()

visited = []
dfs(v)
print()
visited = []
bfs(v)
