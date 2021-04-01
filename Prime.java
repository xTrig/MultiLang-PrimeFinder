public class Prime {

    public static void main(String[] args) {
        int n = 100000;
        int numPrimes = 0;
        long start = System.currentTimeMillis();
        for(int i = 1; i < n; i++) {
            if(isPrime(i)) {
                numPrimes++;
            }
        }
        long end = System.currentTimeMillis();
        long difference = end - start;
        System.out.println("Found " + numPrimes + " primes in " + difference + "ms");
    }

    private static boolean isPrime(int n) {
        for(int i = 2; i < n / 2; i++) {
            if(n % i == 0) {
                return false;
            }
        }
        return true;
    }
}