MAX_NUM = 0
count = 0

for i in range(0, 9):
    A = int(input())
    if A > MAX_NUM:
        MAX_NUM = A
        count = i+1
        
print(MAX_NUM)
print(count)