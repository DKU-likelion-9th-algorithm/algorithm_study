'''


'''


import sys
import math
import itertools
input = sys.stdin.readline

T = int(input())
result = []

for _ in range(T):
    N = int(input())   # 점의 갯수
    lst = []

    x_total = 0
    y_total = 0
    for _ in range(N):
        x, y = map(int, input().split())
        x_total += x
        y_total += y
        lst.append([x, y])

    res = math.inf
    comb = list(itertools.combinations(lst, N//2))   # 더해야 하는 좌표들의 조합
    comb_len_half = len(comb) // 2
    for c in comb[:comb_len_half]:     # comb의 반을 기준으로 뒤는 앞과 방향만 다른 벡터라 길이는 같게 나옴.(계산할 필요 x)
        x_sum, y_sum = 0, 0

        # 더해야 하는 좌표 총합
        for x, y in c:
            x_sum += x
            y_sum += y

        # 빼야 하는 좌표 총합
        x_dif = x_total-x_sum
        y_dif = y_total-y_sum

        # 최소값과 벡터 길이 계산한 결과 비교 후 최소값 구하기
        res = min(res, math.sqrt((x_sum - x_dif) ** 2 + (y_sum - y_dif) ** 2))
    print(res)