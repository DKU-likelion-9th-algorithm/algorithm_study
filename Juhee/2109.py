# 구현 중

'''
import sys

input = sys.stdin.readline

n = int(input())
univ = []

for _ in range(n):
    pd_list = list(map(int, sys.stdin.readline().split()))
    univ.append(pd_list)

univ.sort(key=lambda x: x[0])
univ.sort(key=lambda x: x[1])

ans = 0
ans += univ[len(univ)-1][0]

for i in range(1, len(univ)):
    if univ[i][1] != univ[i-1][1]:  
        ans += univ[i-1][0]

print(ans)

d같은 것들 중에서 p가 가장 큰것을 골라서 더하여 구하기로 풀려고 했으나
이것이 오답의 원인
ex) (1,1) (10,2) (10,2)
이렬 경우 정답은 1+10=11 이 아닌 10+10

'''
import heapq

n = int(input())
univ = []

for i in range(n):
    pd_list = list(map(int, input().split()))
    univ.append(pd_list)

univ.sort(key=lambda x: (x[1]))
#[[20, 1], [2, 1], [100, 2], [8, 2], [10, 3], [50, 10], [5, 20]]

p_list = []

'''
heapq.heappush(heap, item) : item을 heap에 추가
heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴. 비어 있는 경우 IndexError가 호출됨. 
heapq.heapify(x) : 리스트 x를 즉각적으로 heap으로 변환함 (in linear time, O(N) )
'''

for i in univ:
    heapq.heappush(p_list, i[0])
    # p값을 그때그때 우선순위큐에 넣어주는데
    # 그 목록이 몇일안에 해야하는 마감일을 넘긴 경우
    # 가장 작은 값을 제거해준다.
    if (len(p_list) > i[1]):
        heapq.heappop(p_list)

print(sum(p_list))
