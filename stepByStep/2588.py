A = int(input())
B = int(input())

one = B%10
two = (B%100) / 10
three = (B%1000)/100

print(A*one)
print(A*two)
print(A*three)
print(A*B)