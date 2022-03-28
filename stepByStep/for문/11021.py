T = int(input())
A_list = []
B_list = []

for i in range(0, T):
    A, B = map(int, input().split())
    A_list.append(A)
    B_list.append(B)
    
for i in range(0, T):
    print("Case #{0}:".format(i+1), A_list[i]+B_list[i])