import sys
input = sys.stdin.readline

# 동서남북
direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]

R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]
visited = set()
result = 0


def cal(x, y, cnt):
    global result

    result = max(cnt, result)

    for dx, dy in direction:                    # 방향 확인
        nx = x+dx                               # 다음 x좌표구하기
        ny = y+dy                               # 다음 y좌표구하기
        if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in visited:         # 다음 x,y좌표가 유효한지
            visited.add(board[nx][ny])
            cal(nx, ny, cnt + 1)
            visited.remove(board[nx][ny])


visited.add(board[0][0])
cal(0, 0, 1)
print(result)

'''
백트래킹 중요:
방문 여부를 체크하기 - 재귀 전 visited에 더하고 방문 후 visited에서 빼주기
'''