import random

"""
T is the number of test cases
R is the duplicate of the test cases to follow in loop
N is the number of persons in between Gi-hun and Ali
K is the common height of Gi-hun and Ali
sum_n is the sum of N which should be less than 105 in all the total samples
"""
T = random.randrange(1,106)
R = T
sum_n = 0
def random_k(T):
    """
    This function is used to control the value of N that has to be generated in some limitations such that the sum is less than 105.
    """
    if T<=14:
        return random.randrange(1,8)
    elif T>14 and T<35:
        return random.randrange(2,4)
    elif T>=35 and T<52:
        return random.randrange(1,2)
    elif T>=52:
        return 1
        
# The loop will run until the test cases becomes zero
while (T!=0):
    print('T',T)
    
    N = random_k(R)
    sum_n = sum_n + N
    K = random.randrange(1,106)
    count = 0
    print('N',N)
    print('K',K)
    for i in range(0,N):
        h = random.randrange(1,107)
        print('H',h)
        if h > K:
            count = count+1
    
    print('c',count)
    T = T-1
