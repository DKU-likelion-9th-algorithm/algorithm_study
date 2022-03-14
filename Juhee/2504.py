# https://www.acmicpc.net/problem/2504

'''
(()[[]])([])

곱하기 연산이랑 더하기 연산 있어서 변수를 두개로 놓아야 될 것 같다.
후입선출 LIFO --> 스택
괄호를 열 때 스택에 담고
닫는 괄호 나올 때 계산 후 스택에서 pop

'''

import sys

input = sys.stdin.readline

my_string = input()
stack = []
tmp = 1  # 곱하기
ans = 0  # 더하기


for i in range(len(my_string)):
    if my_string[i] == "(":
        stack.append(my_string[i])
        tmp *= 2
    elif my_string[i] == ")":
        if not stack or stack[-1] == "[":  # 잘못된 식
            ans = 0
            break
        if my_string[i-1] == "(":
            ans += tmp
        stack.pop()
        tmp //= 2  # 다시 원래대로
    elif my_string[i] == "[":
        stack.append(my_string[i])
        tmp *= 3
    elif my_string[i] == "]":
        if not stack or stack[-1] == "(":
            ans = 0
            break
        if my_string[i-1] == "[":
            ans += tmp
        stack.pop()
        tmp //= 3  # 다시 원래대로

if stack:  # 잘못된 배열 들어왔을 때. 제대로 된 배열이 들어오게 될 경우 모두 pop
    print(0)
else:
    print(ans)
