#ifndef UTILS_H
#define UTILS_H

#include "Utils.h"
#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <bits/stdc++.h>
#include <unordered_map>

using namespace std;

void sieve(int limit, bool arr[]);
bool isprime(long long int n);
bool millerRabin(long long int n, int bases[], int size);
int bisect(int arr[], int l, int r, int x);
int power(long long int base, long long int exp, long long int modulus);
bool isSquare(long long int n);
long long int gcd(long long int a, long long int b);
int pollardG(int base, int n);
int nextFact(int n);
// TODO make them return vector or map
void primefactors(long long int n, vector<long long int> & factors);
void primefactorsMap(long long int n, unordered_map<long long int, int> & factors);
string reverseString(string s);
void triplets(int s, vector<vector<int>> & sol);
int divisorFuntion(int n);
long long int factorial(int n);
int sumProperDivisors(int n);
int eulerTotient(int n);
bool isPerfectPower(int n);
bool isPandigital(int n);
string fromDez(int n, int b);
int toDez(string s, int b);

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

bool millerRabin(long long int n, int bases[], int size){
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
    if (millerRabin(n, bases, 2)){
      return true;
    }
  }
  else if (n<9080191){
    int bases[] = {31, 73};
    return millerRabin(n, bases, 2);
  }
  else if (n<25326001){
    int bases[] = {2,3,5};
    return millerRabin(n, bases, 3);
  }
  else if (n<3215031751){
    int bases[] = {2,3,5,7};
    return millerRabin(n, bases, 4);
  }
  else if (n<4759123141){
    int bases[] = {2,7,61};
    return millerRabin(n, bases, 3);
  }
  else if (n<1122004669633){
    int bases[] = {2,13,23,1662803};
    return millerRabin(n, bases, 4);
  }
  else if (n<2152302898747){
    int bases[] = {2,3,5,7,11};
    return millerRabin(n, bases, 5);
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
  arguments are the upperbound (exluded)
  and a bool array of length limit
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

bool isSquare(long long int n) {
    if (n < 0)
        return false;
    int root = round(sqrt(n));
    return n == root * root;
}

long long int gcd(long long int a, long long int b){
  long long int temp;
  while (b){
    temp = a;
    a = b;
    b = temp%b;
  }
  return a;
}

int pollardG(int base, int n){
  return fmod(base*base+1,n);
}

int nextFact(long long int n){
  // using the pollard-rho-algorithm
  // https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm
  // returns one factor
  int c = 1;
  while (1) {
    long long int h = 1, t = 1, d = 1;
    while (d == 1) {
      h = (h*h+c) % n;
      h = (h*h+c) % n;
      t = (t*t+c) % n;
      d = gcd(abs(t-h), n);
    }
    if (d != n) {
      return d;
    }
    c++;
  }
}

void primefactors(long long int n, vector<long long int> & factors){
  int primes[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
    43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
    109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
    181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251,
    257, 263, 269, 271, 277, 281, 283, 293};
  // trial divison
  int i = 0;
  int p;
  while (i<62 and n!=1){ // length of primes
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
    if (n != 1){
      factors.push_back(n);
    }
  }
  else{ // pollard rho
    while (!isprime(n)){
      if (isSquare(n)) {
        int f = round(sqrt(n));
        factors.push_back(f);
        n = n/f;
        break;
      }
      int f = nextFact(n);
      factors.push_back(f);
      n = n/f;
    }
    factors.push_back(n);
  }
}

void primefactorsMap(long long int n, unordered_map<long long int, int> & factors) {
  int primes[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
    43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
    109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
    181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251,
    257, 263, 269, 271, 277, 281, 283, 293};
  // trial divison
  int i = 0;
  int p;
  while (i<62 and n!=1){ // length of primes
    p = primes[i];
    if (n%p == 0){
      factors[p] += 1;
      n = n/p;
    }
    else{
      i++;
    }
  }
  if (300*300 > n){
    if (n != 1){
      factors[n] = 1;
    }
  }
  else{ // pollard rho
    while (!isprime(n)){
      if (isSquare(n)) {
        int f = round(sqrt(n));
        factors[f] += 1;
        n = n/f;
        break;
      }
      int f = nextFact(n);
      factors[f] += 1;
      n = n/f;
    }
    factors[n] += 1;
  }
}

string intToString(int n){
  std::string s;
  std::stringstream out;
  out << n;
  return out.str();
}

string reverseString(string s){
    reverse(s.begin(), s.end());
    return s;
}

bool isPalindrom(int n){
  string s = intToString(n);
  return (s == reverseString(s));
}

bool isPalindrom(string s){
  return (s == reverseString(s));
}

void triplets(int s, vector<vector<int>> & sol){
  // adds all primitive triplets with a+b+c = s to sol
  // according to https://projecteuler.net/overview=009
  int half = s/2;
  int lim = ceil(sqrt(s));
  int sm, k, d, n, a, b, c;
  for (int m=2; m<lim; m++){
    if (half % m == 0){
      sm = half/m;
      // remove all factors of 2
      while (sm % 2 == 0){
        sm = sm/2;
      }
      k = m%2 == 1 ? m+2 : m+1;
      while (k < 2*m & k <= sm){
        if (sm%k == 0 & gcd(k, m) == 1){
          d = half/(k*m);
          n = k-m;
          a = d*(m*m - n*n);
          b = 2*d*m*n;
          c = d*(m*m + n*n);
          sol.push_back({a,b,c});
        }
        k = k+2;
      }
    }
  }
}

int divisorFuntion(int n){
  // is the product of the number of occurences of every unique primefactor+1
  // vector of primefactors
  vector<long long int> facts;
  primefactors(n, facts);
  int last = 0;
  int count = 0;
  int product = 1;
  for (auto i: facts) {
    if (i != last) {
      product *= (count + 1);
      count = 1;
      last = i;
    }
    else
      count++;
  }
  product *= (count + 1);
  return product;
}

long long int factorial(int n) {
  long long int first[11] = {1,1,2,6,24,120,720,5040,40320,362880,3628800};
  if (n<11)
    return first[n];
  long long int x = 3628800;
  for (int i=11; i<=n; i++) {
    x *= i;
  }
  return x;
}

int sumProperDivisors(int n) {
  unordered_map<long long int, int> factors;
  primefactorsMap(n, factors);
  double product = 1;
  for (auto pair: factors) {
    product = product * (pow(pair.first, pair.second+1)-1)/(pair.first-1);
  }
  return product;
}

int eulerTotient(int n) {
  vector<long long int> factors;
  primefactors(n, factors);
  double product = 1;
  int last = 0;
  for (auto i: factors) {
    if (i != last) {
      product *= (1-(1.0/i));
      last = i;
    }
  }
  return round(product * n);
}

bool isPerfectPower(int n) {
  int root = round(sqrt(n));
  for (int base=2; base<root+1; base++) {
    double l = log(n)/log(base);
    if (l == floor(l))
      return true;
  }
  return false;
}

bool isPandigital(int n) {
  bool digits[] = {true, false, false, false, false, false, false, false, false, false};
  while (n) {
    int mod = n%10;
    digits[mod] = true;
    n = (n-mod)/10;
  }
  for (int i=1; i<10; i++) {
    if (!digits[i])
      return false;
  }
  return true;
}

string fromDez(int n, int b) {
  char symbols[] = {'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'};
  string s = "";
  int mod = 0;
  while (n>0) {
    mod = n%b;
    s = symbols[mod] + s;
    n = n/b;
  }
  return s;
}

int toDez(string s, int b) {
  int n = 0;
  for (auto c: s) {
    n = b*n + (int) c - 48;
  }
  return n;
}

#endif
