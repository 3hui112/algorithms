T = int(input())

for i in (1, T):
    A, B = map(int, input().split())
    print("Case #{0}:".format(i), A+B)