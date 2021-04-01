import time
import math

def main():
    n = 100000
    numPrimes = 0
    start = time.clock()
    for i in range(1, n):
        if(isPrime(i)):
            numPrimes += 1
    end = time.clock()
    msec = (end - start) * 1000
    print("Found ", numPrimes, " primes in ", msec, "ms")

def isPrime(num):
    for i in range(2, int(math.sqrt(num))):
        if(num % i == 0):
            return False
    return True
main()