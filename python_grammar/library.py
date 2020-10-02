result = sum([1,2,3,4,5])
print(result)

#min(), max()
min_result = min(7,3,5,2)
max_result = max(7,3,5,2)
print(min_result, max_result)

#eval
result = eval("(3+5)*7")
print(result)

#sorted()
result = sorted([9,1,8,5,4])
reverse_result=sorted([9,1,8,5,4],reverse=True)
print(result)
print(reverse_result)

#sorted() with key
array=[('홍길동',35), ('이순신',75), ('아무개',50)]

result = sorted(array, key=lambda x:x[1], reverse=True)
print(result)

#순열
from itertools import permutations

data=['A','B','C']
result = list(permutations(data,3))
print(result)

#조합
from itertools import combinations
result=list(combinations(data,2))
print(result)

#중복순열
from itertools import product
result=list(product(data,repeat=2))
print(result)

#중복 조합
from itertools import combinations_with_replacement

result = list(combinations_with_replacement(data,2))
print(result)

#counter
from collections import Counter

counter=Counter(['red','blue','red','green','blue','blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter))

import math
#최소 공배수(LCM)을 구하는 함수
def lcm(a,b):
    return a*b//math.gcd(a,b)

a=21
b=14
print(math.gcd(21,14))
print(lcm(21,14))