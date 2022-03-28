# https://www.acmicpc.net/problem/2110

'''
이진 탐색: 오름차순으로 정렬된 배열에서 원하는 숫자 찾기
1. 배열 전체 중간값 vs target
2. if 중간값 > target: 왼쪽 비교  right=mid-1
3. 왼쪽 중간값 vs target
반복

target=3
1(left) 2 3 4 6 7(mid) 8 9 10 11 13 14(right) 
1(left) 2 3(mid) 4 6(right)
'''

import sys
input = sys.stdin.readline

N, C = map(int, input().split())
home_list = []

for _ in range(N):
    home_list.append(int(input()))

home_list.sort()


'''
1(O) 2 4(O) 8(O) 9
1부터 시작.
count=1

1(left) 2 3 4 5 6 7 8(right)

mid=(1+8)//2=4
1+4=5
5 이상은 8. 8에 공유기 설치. count=2
--> 그럼 간격을 줄여보자.
right=mid-1
mid=(1+3)//2=2
1+2=3
3 이상은 4. 4에 공유기 설치.
4+3=7
7 이상은 8. 8에 공유기 설치. count=3 성공
'''

# 1(최소 거리 간격.left) ~ 최대 거리 간격(right)


def binary_search():
    left = 1
    right = home_list[-1]-home_list[0]
    while(left <= right):
        mid = (left+right)//2
        count = 1  # 공유기 수
        first = home_list[0]
        for i in range(1, len(home_list)):
            if first+mid <= home_list[i]:
                count += 1
                first = home_list[i]
        if count >= C:
            result = mid
            left = mid+1
        else:
            right = mid-1
    return result


print(binary_search())
