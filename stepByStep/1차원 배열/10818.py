N = int(input())
list = [input().split()]
Max_Num = 0
Min_Num = 0

for i in range (0, N):
    if int(list[i])>Max_Num:
        max_Num = list[i]
    elif int(list[i])<Min_Num:
        min_Num = list[i]

print(min_Num, max_Num)

