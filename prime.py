import time
import math

def main():
    n = 1000000
    numPrimes = 0
    start = time.clock()
    for i in range(1, n):
        if(isPrime(i)):
            numPrimes += 1
    end = time.clock()
    msec = (end - start) * 1000
    print("Found ", numPrimes, " primes in ", msec, "ms")

def isPrime(num):
    maxCheck = int(math.sqrt(num))
    for i in range(2, maxCheck):
        if(num % i == 0):
            return False
    return True

if __name__ == "__main__":
    main()