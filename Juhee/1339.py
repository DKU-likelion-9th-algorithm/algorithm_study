# https://www.acmicpc.net/problem/1339

import sys
input = sys.stdin.readline

N = int(input())

alpha_dict = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0,
              'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
my_list = []
alpha_list = []

for _ in range(N):
    my_list.append(input().rstrip())

# GCF
# ACDEB

for alpha in my_list:
    for i in range(len(alpha)):
        num = 10**(len(alpha)-1-i)
        alpha_dict[alpha[i]] += num

# alpha_dict
# A: 10000, B:1, C:1010, D:100, E:10 F:1, G:100

for value in alpha_dict.values():
    if value > 0:
        alpha_list.append(value)

alpha_list.sort(reverse=True)

# alpha_list
# 10000 1010 100 100 10 1 1

answer = 0

# (10000*9)+(1010*8)+(100*7)+(100*6)+(10*5)+(1*4)+(1*3)
for i in range(len(alpha_list)):
    answer += alpha_list[i]*(9-i)


print(answer)
