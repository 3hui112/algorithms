N = int(input())
new = None
ten = N // 10
one = N % 10
cycle = 0

while new != N:
    new = ten+one
    if new < 10:
        new = (one*10) + new
    else:
        new = (one*10)+(new%10)
    ten = new // 10
    one = new % 10
    cycle = cycle+1
    
print(cycle)