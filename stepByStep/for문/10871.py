N, X = map(int, input().split())
B_List = list()
A_List = map(int, input().split())
A_List = list(A_List)

for i in range (0, N-1):
    if A_List[i] < X:
        B_List.append(A_List[i])
        
for j in range(0, len(B_List)):
    string = ''
    split_strings = string.split()
    split_strings.insert(j, B_List[j])
    String = ' '.join(split_strings)
    
print(String)