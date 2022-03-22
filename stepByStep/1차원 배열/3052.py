import sys

list = []
list_remain = []

lines = sys.stdin.readlines()

for value in lines:
    list.append(int(value))
    list_remain.append(int(value)%42)
    
different = 0

#서로 다른 값 몇 개 있는지...