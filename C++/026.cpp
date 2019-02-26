#include <iostream>
#include <algorithm>
#include <vector>
#include "Utils.h"

using namespace std;

int recurLen(int d) {
  vector<int> v;
  int count = 0;
  int n = 1;
  // written division
  while (1) {
    n *= 10;
    n = n%d;
    auto f = find(v.begin(), v.end(), n);
    if (f != v.end()) {
      return count-(f-v.begin());
    }
    v.push_back(n);
    count++;
  }
}

int main() {
  int limit = 1000;
  int res = 0;
  int resIndex = 0;
  bool primes[limit];
  sieve(limit, primes);

  for (int i=limit-1; i>=0; i--) {
    if (primes[i] == true) { // if isprime
      int len = recurLen(i);
      if (len > res) {
        res = len;
        resIndex = i;
      }
      else
        break;
    }
  }
  cout << resIndex;

}
