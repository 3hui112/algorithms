A, B, C = map(int, input().split())

if A == B:
    if A == C:
        reward = 10000 + 1000*A #셋 다 같을 경우
    elif A != C:
        reward = 1000 + 100*A # A=B
elif A == C:
    reward = 1000 + 100*A # A=C
elif B == C:
    reward = 1000 + 100*B # B=C
else:
    if A>B:
        if A>C:
            biggest = A
        else:
            biggest = C
    elif B>C:
        biggest = B
    elif C>B:
        biggest = C
    reward = biggest * 100
    
print(reward)
    
    