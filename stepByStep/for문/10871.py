N, X = map(int, input().split())
A_list = list(map(int, input().split()))
less_than_X = []

for i in range (0, N):
    if A_list[i] < X:
        less_than_X.append(A_list[i])
    
print(' '.join(str(x) for x in less_than_X))