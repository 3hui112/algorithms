line_list = []
line = input()

while line != "0 0":
    line_list.append(line)
    line = input()
    
for line in line_list:
    A, B = map(int, line.split())
    print(A+B)