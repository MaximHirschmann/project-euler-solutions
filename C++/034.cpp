#include <iostream>

using namespace std;

int sumFactorialDigits(int n) {
  int fac[] = {1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880};
  int sum = 0;
  while (n) {
    int mod = n%10;
    sum += fac[mod];
    n = (n-mod)/10;
  }
  return sum;
}

int main() {
  int sum = 0;
  for (int i=3; i<2540160; i++) {
    if (i == sumFactorialDigits(i))
      sum += i;
  }
  cout << sum;
}
