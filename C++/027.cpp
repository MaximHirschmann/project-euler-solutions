#include <iostream>
#include "Utils.h"

using namespace std;

// where f(n) = n^2 + a*n + b
int numberPrimes(int a, int b) {
  int n = 0;
  while (isprime(n*n + n*a + b))
    n++;
  return n;
}

int main() {
  int max = 0;
  int prod = 0;
  int limit = 1000;
  bool primes[limit];
  sieve(limit, primes);

  // a has to be odd
  for (int a=-1* (limit-1); a<limit; a+=2) {
    // b has to be prime otherwise f(0) would not be prime
    // b can not be negative
    // a >= 1-b because n^2 + a*n + b >= 2 and if n=1 then 1+a+n >= 2
    for (int b=limit-1; b>=0; b--) {
      if (primes[b]) {
        if (a < 1-b)
          break;
        int num = numberPrimes(a,b);
        if (num > max) {
          max = num;
          prod = a*b;
        }
      }
    }
  }
  cout << prod << " " << max;
}
