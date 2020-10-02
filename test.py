#python list 기본 문법
a=[1,2,3,4,5]
print(a)

a=[i for i in range(10)]
print(a)

#0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]

print(array)

#1부터 9까지의 수들의 제곱 값을 포함하는 리스트
array=[i*i for i in range(1,10)]

print(array)

#리스트 컴프리헨션
#0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]
print(array)

#일반적인 코드
array=[]
for i in range(20):
  if i%2 ==1:
    array.append(i)

print(array)

#리스트 컴프리헨션 N*M크기의 2차원 리스트 초기화
n=4
m=3
array=[[0]*m for _ in range(n)]
print(array)

#잘못된 예시
array=[[0]*m]*n
#내부적 데이터를 모두 하나의 객체로 인식
print(array)
array[1][1]=5
print(array)


#리스트 관련 메서드