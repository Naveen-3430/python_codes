import random
T = random.randrange(1,106)
R = T
sum_n = 0
def random_k(T):
    if T<=14:
        return random.randrange(1,8)
    elif T>14 and T<35:
        return random.randrange(2,4)
    elif T>=35 and T<52:
        return random.randrange(1,2)
    elif T>=52:
        return 1
        

while (T!=0):
    print(T)
    
    N = random_k(R)
    sum_n = sum_n + N
    K = random.randrange(1,106)
    count = 0
    print('n',N)
    print('k',K)
    for i in range(0,N):
        h = random.randrange(1,107)
        print('h',h)
        if h > K:
            count = count+1
    
    print('c',count)
    T = T-1
