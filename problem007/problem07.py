import numpy as np

def isPrime(n):
    if(n<4):
        return True;
    else:
        a = np.sqrt(n)
        i = 2
        while (i<=a):
            if(n%i == 0):
                return False
            i = i+1
        return True

counter = 1
n = 2
while(counter<=10001):
    if(isPrime(n)):
        counter+=1 
    if(counter<=10001):
        n+=1

print(n)

# the answer is 104743