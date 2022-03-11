##첫째 줄에는 현재 시각이 나온다.
##현재 시각은 시 A (0 ≤ A ≤ 23) 와 분 B (0 ≤ B ≤ 59)가 정수로 빈칸을 사이에 두고 순서대로 주어진다.
##두 번째 줄에는 요리하는 데 필요한 시간 C (0 ≤ C ≤ 1,000)가 분 단위로 주어진다.

A, B = map(int, input().split())
C = int(input())

if B+C >= 60:
    hour = A + ((B+C))//60
    minute = (B+C)%60
    if hour > 23:
        hour = hour % 24
else:
    hour = A
    minute = B+C
    
print(hour, minute)