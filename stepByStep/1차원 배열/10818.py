N = int(input())
list = list(map(int, input().split()))
max_Num = list[0]
min_Num = list[0]

for i in range (0, N):
    if int(list[i])>max_Num:
        max_Num = list[i]
    elif int(list[i])<min_Num:
        min_Num = list[i]

print(min_Num, max_Num)