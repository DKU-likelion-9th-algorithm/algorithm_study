import sys
sys.setrecursionlimit(10 ** 9)

# 입력 및 변수 초기화
direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]
ground = []   # 입력받은 배열
result = 1    # 최대 물에 잠기지 않은 영역의 개수 (아무 지역도 물에 잠기지 않을 때인 1 로 초기화)
responce = 0  # 각 물높이에서의 물에 잠기지 않은 영역의 개수

N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    ground.append(list(map(int, sys.stdin.readline().split())))

h = max(max(ground))


def cal(x, y):
    if board[x][y] != -1:
        return
    board[x][y] = 0                            # 방문했다 표시.

    # 갈 수 있는 길 끝까지 방문해 전부 방문표시를 한다. (다시 방문하지 않게)
    for dx, dy in direction:
        nx = x + dx                               # 다음 x좌표구하기
        ny = y + dy                               # 다음 y좌표구하기

        if 0 <= nx < N and 0 <= ny < N:         # 다음 x, r좌표가 유효한지
            if ground[nx][ny] > water and board[nx][ny] == -1:
                cal(nx, ny)


# 계산하기
for water in range(1, h):   # water: 물높이, 물 높이 N~100는 물에 잠기지 않는 영역이 0이라 계산 x.
    board = [[-1] * N for _ in range(N)]        # board(방문했는지) 초기화
    for j in range(N):
        for k in range(N):
            if ground[j][k] > water and board[j][k] == -1:
                responce = responce + 1
                cal(j, k)
    result = max(result, responce)
    responce = 0

print(result)


'''
풀이 생각 과정
4963번과 비슷하다고 생각한다. 다른 점은 board 초기화 위치인 것 같다.
'''
