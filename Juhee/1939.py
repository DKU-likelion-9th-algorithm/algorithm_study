from collections import deque
import sys
input = sys.stdin.readline


def bfs(mid):
    visit[i1] = 1
    q = deque()
    q.append(i1)
    while q:
        start = q.popleft()
        # 끝까지 돌았을 경우
        if start == i2:
            return True
        for nx, nc in s[start]:
            # 아직 방문 안했고 현재 무게 nc로 갈 수 있다면 추가탐색
            if visit[nx] == 0 and mid <= nc:
                q.append(nx)
                visit[nx] = 1
    return False


n, m = map(int, input().split())
s = [[] for i in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    s[a].append([b, c])
    s[b].append([a, c])

#[[], [[2, 2], [3, 3]], [[1, 2], [3, 2]], [[1, 3], [2, 2]]]

i1, i2 = map(int, input().split())  # 1, 3
low, high = 1, 1000000000

while low <= high:
    visit = [0 for i in range(n + 1)]
    mid = (low + high) // 2
    # 해당 무게로 i1 --> i2까지 도착 가능하면
    if bfs(mid):
        low = mid + 1
    else:
        high = mid - 1
print(high)
