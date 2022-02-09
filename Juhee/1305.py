# https://www.acmicpc.net/problem/1305
# https://devbull.xyz/python-kmp-algorijeumeuro-munjayeol-cajgi/

import sys

input = sys.stdin.readline

L = int(input())  # 6
S = input().rstrip()  # aabaaa

pattern_table = [0 for _ in range(L)]
j = 0
i = 1

'''
while i < L:
    # 이전 인덱스에서 같았다면 다음 인덱스만 비교
    if S[i] == S[j]:
        j += 1
        pattern_table[i] = j
        i += 1
    else:
        if j != 0:
            # 이전 인덱스에서는 같았으므로 j을 줄여서 다시 검사
            j = pattern_table[j-1]
            # 다시 검사해야 하므로 i는 증가하지 않음
        else:
            # 이전 인덱스에서도 같지 않았다면 pattern_table[i]는 0 이고 i는 1 증가
            pattern_table[i] = 0
            i += 1

'''

for i in range(1, L):
    while j > 0 and S[i] != S[j]:
        j = pattern_table[j-1]
    if S[i] == S[j]:
        j += 1
        pattern_table[i] = j


ans = L-pattern_table[L-1]
print(ans)
