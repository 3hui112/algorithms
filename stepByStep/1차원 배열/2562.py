MAX_NUM = 0
count = -1

while True:
    A = int(input())
    if A > MAX_NUM:
        MAX_NUM = A
        count = count + 1
        
print(MAX_NUM)
print(count)