'''
jew = [(1, 20), (2, 100), (5, 50)]

각 가방에 넣을 수 있는 보석 중 가장 가치 높은 보석을 넣기
bags 순서 = [10, 2]              :  10에 가치 100보석, 2에 가치 20 보석 = 총 가치 120
                    -> [2, 10]  :  2에 가치 100 보석, 10에 가치 50 보석 = 총 가치 150
따라서 가방에 넣을 수 있는 무게가 작은 순으로, ( 2 다음 10 넣기 )
각 가방에 넣을 수 있는 가장 큰 가치 보석을 넣기
'''

import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
jew = []
for _ in range(N):
    heapq.heappush(jew, list(map(int, input().split())))

bags = []
for _ in range(K):
    bags.append(int(input()))
bags.sort()

res = 0
value_jew = []

for bag in bags:
    # 현재 가방에 넣을 수 있는 보석들 모두 찾기
    while jew and bag >= jew[0][0]:  # 무게가 작은 순으로 정렬됨
        [weight, value] = heapq.heappop(jew)  # 최소 무게부터 차례대로 꺼낸다
        heapq.heappush(value_jew, -value)  # 보석 가치만 최대힙으로 넣어준다.

    # 각 가방마다 넣을 수 있는 보석 중 가치가 가장 높은 보석 넣기
    if value_jew:
        # (heapq.push할 때 최대 힙을 사용하기 위해-로 넣어줬으니까 음수에 -해서 더하기로 만들어줌)
        res -= heapq.heappop(value_jew)  # 가장 가치가 큰 보석의 가치만 더해주기
    elif not jew:  # 가방이 보석보다 많을 때
        break

print(res)


'''
heapq(최소 힙)는 index 0만 가장 작은 수가 오도록 한다.
가장 작은 수가 있지 않으면 가장 작은 수와 index 0 원소의 자리를 바꾼다.
'''