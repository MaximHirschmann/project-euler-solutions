#include "Utils.h"
#include <iostream>
#include <cmath>
#include <vector>
#include <string>

using namespace std;

void sieve(int limit, bool arr[]);
bool isprime(long long int n)
bool miller_rabin(long long int n, int bases[], int size)
int bisect(int arr[], int l, int r, int x);
int power(long long int base, long long int exp, long long int modulus);
int gcd(int a, int b);
int pollard_g(int base, int n);
int next_fact(int n);
void primefactors(int n);
bool isPalindrom(int n);

int power(long long int base, long long int exp, long long int modulus) {
  base %= modulus;
  int result = 1;

  while (exp > 0) {
    if (exp % 2 == 1){
      result = (result * base) % modulus;
    }
    base = (base * base) % modulus;
    exp >>= 1;
  }
  return result;
}

bool miller_rabin(long long int n, int bases[], int size){
  // primality test with the miller_rabin method
  // represent n-1 as d * 2^s
  int temp = n-1;
  long long int s = 0;
  while (temp%2 == 0){
    s++;
    temp = temp/2;
  }
  long long d = (n-1)/(pow(2, s));
  for (int i=0; i<size; i++){
    int a = bases[i]; // a is the base
    if (power(a,d,n) != 1){
      bool all = true;
      for (long long int r=0; r<s; r++){
        if (power(a, pow(2, r)*d, n) == n-1){
          all = false;
          break;
        }
      }
      if (all){
        return false;
      }
    }
  }
  return true;
}

bool isprime(long long int n){
  // checking simple cases first
  if (n==2 | n==3 | n==5){
    return true;
  }
  if (n < 2 | n%2==0 | n%3==0 | n%5==0){
    return false;
  }
  if (n<49){
    return true;
  }
  if (n%7==0 | n%11==0 | n%13==0 | n%17==0 |
    n%19==0 | n%23==0 | n%29==0 | n%31==0 |
    n%37==0 | n%41==0 || n%43==0 || n%47==0){
      return false;
  }
  if (n<2809){
    return true;
  }
  if (n <= 23001){
    int exc[] = {341, 561, 645, 1105, 1387, 1729,1905, 2047, 2465, 2701,
      2821, 3277, 4033, 4369, 4371, 4681, 5461, 6601, 7957, 8321, 8481, 8911,
      10261, 10585, 11305, 12801, 13741, 13747, 13981, 14491, 15709, 15841,
      16705, 18705, 18721, 19951, 23001};
    return (power(2,n,n) == 2 & bisect(exc, 0, sizeof(exc)/sizeof(int), n) == -1);
  }
  // using Miller Rabin primality test
  // a list of bases are here:
  // https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Computational_complexity
  if (n<1373653){
    int bases[] = {2, 3};
    if (miller_rabin(n, bases, 2)){
      return true;
    }
  }
  else if (n<9080191){
    int bases[] = {31, 73};
    return miller_rabin(n, bases, 2);
  }
  else if (n<25326001){
    int bases[] = {2,3,5};
    return miller_rabin(n, bases, 3);
  }
  else if (n<3215031751){
    int bases[] = {2,3,5,7};
    return miller_rabin(n, bases, 4);
  }
  else if (n<4759123141){
    int bases[] = {2,7,61}:
    return miller_rabin(n, bases, 3);
  }
  else if (n<1122004669633){
    int bases[] = {2,13,23,1662803};
    return miller_rabin(n, bases, 4);
  }
  else if (n<2152302898747){
    int bases[] = {2,3,5,7,11};
    return miller_rabin(n, bases, 5);
  }
  return false;
}

int bisect(int arr[], int l, int r, int x){
  // returns index of element x in array
  // if x not in array returns -1
  if (r >= l) {
      int mid = l + (r - l) / 2;
      if (arr[mid] == x)
          return mid;
      if (arr[mid] > x)
          return bisect(arr, l, mid - 1, x);
      return bisect(arr, mid + 1, r, x);
  }
  return -1;
}

void sieve(int limit, bool arr[]){
  /*
    example:
      int limit = 100;
      bool arr[limit];
      sieve(limit, arr);
      for (int i=0;i<limit;i++){
        if (arr[i]){
          std::cout << i << ",";
        }
      }
  */
  // index is the value, the value is whether it is a prime
  // set all values to true except 0 and 1
  for (int i=0;i<limit;i++){
    arr[i] = true;
  }
  arr[0] = false;
  arr[1] = false;
  int i = 0;
  while (i*i < limit){
    if (arr[i] == true){  //i is prime
      // mark multiples
      int k = 2;
      for (int k=2; k <= limit/i; k++){
        arr[k*i] = false;
      }
    }
    i++;
  }
}

int gcd(int a, int b){
  int temp;
  while (b){
    temp = a;
    a = b;
    b = temp%b;
  }
  return a;
}

int pollard_g(int base, int n){
  return fmod(base*base+1,n);
}

int next_fact(int n){
  // using the pollard-rho-algorithm
  // https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm
  // returns one factor
  // if failed to find a factor
  double x = 2;
  double y = 2;
  double d = 1;
  while (d==1){
    x = pollard_g(x, n);
    y = pollard_g(pollard_g(y,n),n);
    d = gcd(abs(x-y), n);
  }
  if (d==n){
    return next_fact(n);
  }
  return d;
}

void primefactors(long long int n, vector<int> & factors){
  if (isprime(n)){
    factors = {n};
  }
  else{
    int primes[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
      43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
      109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
      181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251,
      257, 263, 269, 271, 277, 281, 283, 293};
    // trial divison
    int i = 0;
    int p;
    while (i<62){ // length of primes
      p = primes[i];
      if (n%p == 0){
        factors.push_back(p);
        n = n/p;
      }
      else{
        i++;
      }
    }
    if (300*300 > n){
      factors.push_back(n);
    }
    else{ // pollard rho
      while (!isprime(n)){
        int f = next_fact(n);
        factors.push_back(f);
        n = n/f;
      }
      factors.push_back(n);
    }
  }
}
