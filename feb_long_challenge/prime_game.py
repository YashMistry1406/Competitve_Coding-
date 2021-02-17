def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        # If prime[p] is not 
        # changed, then it is a prime
        if (prime[p] == True):
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    return len(prime)
if __name__ == '__main__':

    for i in range (int(input())):

        x,y=map(int,input().split())


        if SieveOfEratosthenes(x)>y:
            print("Divyam")
        else:
            print("Chef")


