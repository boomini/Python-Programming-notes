#데이터의 개수 입력
n = int(input())
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)

for i in data:
  print(i)

#문자열 입력받기
import sys
data = sys.stdin.readline().rstrip()
print(data)

#출력할 변수들
a=1
b=2
print(a,b)
print(7,end=" ")
print(8,end=" ")

출력할 변수들
answer=7
print("정답은 "+str(answer)+"입니다.")

#파이썬 3.6부터 가능, f-string
answer=7
print=(f"정답은 {answer}입니다")