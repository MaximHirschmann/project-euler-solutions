#include <iostream>
#include <vector>
#include "Utils.h"

using namespace std;

int main() {
  
  int limit = 28123;
  vector<int> abundant;
  bool sums[limit+1];
  for (int i=12; i<limit; i++) {
    int s = sumProperDivisors(i)-i;
    if (s > i)
      abundant.push_back(i);
  }

  for (int i=0; i<abundant.size(); i++) {
    for (int j=i; j<abundant.size(); j++) {
      int sumsAbundant = abundant[i] + abundant[j];
      if (sumsAbundant > limit)
        break;
      sums[sumsAbundant] = true;
    }
  }

  int res = 0;
  for (int i=1; i<=limit; i++) {
    if (sums[i] == false)
      res += i;
  }
  cout << res << "\n";
}
