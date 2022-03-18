N = int(input())
grade = input().split()

M = grade[0]

for j in range(0, N):
    if M < grade[j]:
        M = grade[j]

trans_grade = []
sum = 0

for i in range(0, N):
    trans_grade.append((int(grade[i])/int(M))*100)
    sum = sum + trans_grade[i]
    
print(M)
print(trans_grade)
mean = sum/N
print(mean)