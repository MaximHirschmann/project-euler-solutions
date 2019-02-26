#include "Utils.h"
#include <algorithm>

using namespace std;

string rotate(string s) {
  // "hello world" --> "dhello worl"
  int length = s.size();
  string res = "";
  res += s[length-1];
  res += s.substr(0, length-1);
  return res;
}

int main() {
  int limit = 1000000;
  bool primes[limit];
  sieve(limit, primes);
  vector<string> circPrimes; // circular primes

  for (int i=0; i<limit; i++) {
    if (primes[i]) {
      string s = intToString(i);
      // check if s in circPrimes to avoid duplicates
      if (find(circPrimes.begin(), circPrimes.end(), s) == circPrimes.end()) {
        string rotations[s.size()];
        bool is = true; // whether s is a circular prime
        for (int j=0; j<s.size(); j++) {
          s = rotate(s);
          rotations[j] = s;
          if (primes[stoi(s)] == false) { // if not prime
            is = false;
            break;
          }
        }
        if (is) {
          // add s and rotations of s to circPrimes
          for (auto j: rotations) {
            circPrimes.push_back(j);
          }
        }
      }
    }
  }
  float res = circPrimes.size(); // number of UNIQUE elements in circPrimes
  for (auto i: circPrimes) {
    int num = count(circPrimes.begin(), circPrimes.end(), i);
    if (num > 1)
      res = res - (1.0/num);
  }
  cout << float(res) << "\n";
}
