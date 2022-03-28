import sys
input = sys.stdin.readline

'''     
       C1 C2 C3 C4
list : 40 30 30 50              table[i][j] : i에서 j까지의 파일을 합치는 최소 비용
 
길이 1 : 비용 들지 않음
table[1][1] : 0
table[2][2] : 0
table[3][3] : 0
table[4][4] : 0

길이 2 : 
table[1][2] : list[1]+list[2] = 70
table[2][3] : list[2]+list[3] = 60
table[3][4] : list[3]+list[4] = 80

길이 3 : min (2인 길이를 더하는 방법 중에 젤 작은 비용 + 길이 3인 파일 다 더하기)
(1 + 2,3), (1,2 + 3)
table[1][3] : min(0+60, 70+0) + 100 = 160 
(2, + 3,4), (2,3 + 4)
table[2][4] : min(0+80, 60+0) + 110 = 170

길이 4 : 
(1 +,2,3,4), (1,2 + 3,4), (1,2,3 + 4)
table[1][4] : min(0 + 170, 70 + 80, 160 + 0) + 150 = 300

점화식   table[i][j] : min(list[i][k] + list[k+1][j]) + sum(list[i]~list[j])
'''
T = int(input())
for _ in range(T):
    N = int(input())
    lst = [0] + list(map(int, input().split()))

    S = [0 for _ in range(N+1)]  # 1부터 i까지의 누적합
    for i in range(1, N+1):      # 누적 합을 구하는 이유 : 나중에 계속 i부터 j까지의 누적합을 이용해야하기 때문
        S[i] = S[i-1] + lst[i]

    table = [[0 for _ in range(N+1)] for _ in range(N+1)]

    for i in range(2, N+1):         # 부분 파일의 길이 (길이 1은 어차피 0)
        for j in range(1, N+2-i):   # 시작점
            table[j][j+i-1] = min([table[j][j+k] + table[j+k+1][j+i-1] for k in range(i-1)]) + (S[j+i-1]-S[j-1])  # 점화식

    print(table[1][N])

''' 순서 유지 X
T = int(input())
for _ in range(T):
    N = int(input())
    res = 0
    q = list(map(int, input().split()))

    heapq.heapify(q)

    while len(q) != 1:
        cnt1 = heapq.heappop(q)
        cnt2 = heapq.heappop(q)
        heapq.heappush(q, cnt1+cnt2)
        res = cnt1 + cnt2 + res
    print(res)

'''