# 백준 2470 - 두 용액(https://www.acmicpc.net/problem/2470)

"""
문제 : 두 용액의 특성값 합이 가장 0에 가까운 걸 찾아서 각 용액의 특성값을 오름차순 출력
이 때 산성용액끼리, 알칼리 용액끼리의 합도 정답으로 가능함

0에서 가장 가까운 = 절댓값이 가장 작은
-> abs()사용

브루트하게 푸는 법: N개의 용액들에 대해 첫 용액부터 순차적으로 돌면서 가장 절댓값이 작은 걸 찾고, 마지막엔 찾은 것 중 가장 작은 걸 가져온다
-> N이 10만이 주어지면 반복문이 10만 X 10만 = 100억번 돌려지는데 시간초과 뜰 것 같음. 

일단 입력된 상태로 그면 뒤죽박죽이라 어떠한 방법도 쓸 수 없을 것 같아서
정렬한 뒤에 하면 뭔가 될 것 같음. 

주어진 특성값들이 모두 양수 -> 가장 작은 놈 두 개가 정답
주어진 특성값들이 모두 음수 -> 가장 큰 놈 두 개가 정답
특성값들이 양, 음수 섞여있  -> 각 끝 점 잡고 찾기 

특성값들이 양, 음수가 섞여있다면
각 끝점을 잡고, 이들의 합을 구함

각 끝점을 비교해 절댓값이 큰 쪽의 점을 한 칸씩 이동하면서 새로 합을 구한다.
절댓값이 작은 쪽의 점을 이동하면 새로 구하는 합이 오히려 더 커짐. 



"""

import sys
n = int(sys.stdin.readline())
val = list(map(int, sys.stdin.readline().split()))
val.sort()

if val[0] > 0:                  # 정렬한 뒤 첫 값이 양수 -> 특성값이 모두 양수   
    print(val[0], val[1])
elif val[-1] < 0:               # 정렬한 뒤 마지막 값이 음수 -> 특성값이 모두 음수
    print(val[-2], val[-1])
else:                                  
    i, j = 0, len(val) - 1                    # 최초 시작시 끝점
    answer_i, answer_j = i, j                 # 정답이 될 점들
    answer_sum = abs(val[i] + val[j])         # 최초 시작 시 두 끝점의 합의 절댓값
    while(i < j - 1):                         # i, j가 같아지면 안되므로
        if abs(val[i]) > abs(val[j]):
            i += 1
        elif abs(val[i]) < abs(val[j]):
            j -= 1
        else:         # 두 개의 절댓값 같음 = 합이 0인 경우 -> 정답
            break
        if abs(val[i] + val[j]) < answer_sum:     # 새로 구한 합의 절댓값이 더 작다면
            answer_sum = abs(val[i] + val[j])     # 정답이 될 애들 갱신
            answer_i, answer_j = i, j          
    print(val[answer_i], val[answer_j])
