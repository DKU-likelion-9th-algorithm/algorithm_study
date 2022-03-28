'''
        입력 순열 : 1 5 2 1 4 3 4 5 2 1
증가하는 순열의 길이: 1 2 2 1 3 3 4 5 2 1  => [ 1,2,3,4,5 ] (5개)
감소하는 순열의 길이: 1 5 2 1 4 3 3 3 2 1  => [ 5, 2, 1] (3개)
         result : 2 7 4 2 7 6 7 8 4 2
증가하는 순열의 길이와 감소하는 순열의 길이를 더했을 때 가장 큰 값이 가장 긴 바이토닉 수열

[ 1,2,3,4,5,5,2,1] (8개) 5는 중복이니까 총 7개
'''

import sys
input = sys.stdin.readline

n = int(input())

board = list(map(int, input().split()))
reversed_board = board[::-1]

increase = [1 for _ in range(n)]       # 증가하는 순열의 길이
decrease = [1 for _ in range(n)]       # 감소하는 순열의 길이

for i in range(n):
    for j in range(i):           # 앞의 값들과 비교해
        if board[i] > board[j]:  # 현재가 더 크다면 더 작은 값의 증가 순열의 길이+1(현재를 포함해야 하기 때문)과
            # 현재까지의 증가 순열의 길이를 비교해 더 큰값을 넣어줌.
            increase[i] = max(increase[i], increase[j]+1)
        if reversed_board[i] > reversed_board[j]:   # reversed_board가 뒤집어진 상태로 앞부터 비교해
            decrease[i] = max(decrease[i], decrease[j]+1)  # decrease도 앞부터 채워졌기 때문에

result = [0 for _ in range(n)]
for i in range(n):
    result[i] = increase[i] + decrease[n-i-1]

print(max(result)-1)  # -1은 아래 참고

'''
증가하는 수열: 1,2,3,4,5 (5개)
감소하는 수열: 5,2,1  (3개)

5+3, 합을 구하면서 5를 두 번 계산하였으므로 1을 빼주면 정답
'''
