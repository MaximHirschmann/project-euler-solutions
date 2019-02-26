#include <iostream>
#include <unordered_map>
#include "Utils.h"
#include <time.h>

using namespace std;

int main() {
  clock_t start = clock();
  unordered_map<int, int> sums = {{0,0}};
  int res = 0;
  for (int i=2; i<10000; i++) {
    int sum = sumProperDivisors(i)-i;
    sums[i] = sum;
    if (sum<i & sums[sum] == i) {
      res += i+sum;
    }
  }
  cout << res << "\n";
  cout << clock()-start << "ms\n";
}
