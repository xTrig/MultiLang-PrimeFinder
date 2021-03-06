#include <stdio.h>
#include <stdbool.h>
#include <time.h>
#include <math.h>


bool isPrime(int* n) {
    for(int i = 2; i < sqrt(*n); i++) {
        if(*n % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    int n = 1000000;
    int numPrimes = 0;
    clock_t start = clock();
    for(int i = 1; i < n; i++) {
        if(isPrime(&i)) {
            // primes[numPrimes] = i;
            numPrimes++;
        }
    }
    clock_t difference = clock() - start;
    int msec = difference * 1000 / CLOCKS_PER_SEC;
    printf("Found %d prime numbers in %dms", numPrimes, msec);
    return 1;
}