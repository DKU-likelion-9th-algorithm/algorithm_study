'''
풀이 : string을 동일한 0 또는 1로 쪼개고 min(len)으로 합침.
ex) 011001 => token = [0, 11, 00, 1]로 쪼개짐
0과 11은 min(len(0),len(1))=1으로 01이 만들어짐.
11과 00은 min(len(11),len(00))=2으로 10, 1100이 만들어짐.
00과 1은 min(len(00),len(1)) = 1으로 01이 만들어짐.
'''
string = input()

result = 0
token = []
lastIndex = 0

for index in range(1, len(string)):
    print(lastIndex, index, string[lastIndex], string[index])
    if string[lastIndex] != string[index]:
        token.append(string[lastIndex:index])
        lastIndex = index

token.append(string[lastIndex:len(string)])

for index in range(1, len(token)):
    result += min(len(token[index-1]), len(token[index]))

print(result)

'''

이진 부분 문자열 계산
이진 문자열은 0과 1로만 구성된 문자열입니다. 하위 문자열은 문자열 내에서 연속적인 문자 그룹입니다.
이진 문자열이 주어지면 동일한 수의 0과 1을 포함하고 모든 0과 1이 함께 그룹화되는 부분 문자열의 수를 찾으십시오.
중복 부분 문자열도 답변에 포함됩니다. 예를 들어 '0011'에는 '0011'과 '01'이라는 기준을 충족하는 두 개의 겹치는 부분 문자열이 있습니다.

ex)
string = '011001"
하위 문자열 '01', '10', '1100', '01'은 0과 1의 수가 동일하며 모든 0과 1이 연속적으로 그룹화됩니다. 
따라서 답은 4입니다. 
'0110'은 0과 1의 수가 같지만 모든 0과 1이 함께 그룹화되지 않기 때문에 계산되지 않습니다.
'''