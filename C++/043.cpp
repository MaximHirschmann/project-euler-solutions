#include <iostream>
#include <algorithm>
#include "Utils.h"

bool isDivisible(int d[9]) {
  if (d[0] == 0) {
    return false;
  }

  // insert 5 on position 5
  int num[10];
  for (int i=0; i<5; i++) {
    num[i] = d[i];
  }
  num[5] = 5;
  for (int i=5; i<9; i++) {
    num[i+1] = d[i];
  }

  int divisors[] = {2,3,5,7,11,13,17};
  for (int i=0; i<7; i++) {
    if ((num[i+1]*100 + num[i+2]*10 + num[i+3]) % divisors[i] != 0)
      return false;
  }
  return true;
}

long long int arrayToInt(int digits[9]) {
  long long int num = 50000;
  // first 5 digits
  for (int j=0; j<5; j++) {
    num += digits[j] * round(pow(10.0, 9-j));
  }
  // last 4 digits
  for (int j=5; j<10; j++) {
    num += digits[j] * round(pow(10.0, 8-j));
  }
  return num;
}

int main() {
  long long int res = 0;
  long long int num;
  int digits[] = {0,1,2,3,4,6,7,8,9}; // 5 has to be on position 5
  int length = sizeof(digits)/sizeof(int);
  for (int i=0; i<factorial(length); i++) {
    next_permutation(digits, digits+length);
    if (isDivisible(digits)) {
      num = arrayToInt(digits);
      cout << num << "\n";
      res += num;
    }
  }
  cout << res;
}
