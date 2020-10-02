array=[9,8,7,6,5]

for x in array:
  print(x,end=" ")

result = 0
for i in range(1,10):
  result +=i

print(result)

scores=[90,85,77,65,97]
cheating_student_list={2,4}

for i in range(5):
  if i+1 in cheating_student_list:
    continue
  if scores[i] >=80:
    print(i+1,"번 학생은 합격입니다.")

for i in range(2,10):
  for j in range(1,10):
    print(i,"*",j,"=",i*j)
  print()