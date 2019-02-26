#include "Utils.h"

using namespace std;

int concat(int small, int big, int product) {
  int res;
  if (small < 10)
    res = small * 100000000 + big * 10000 + product;
  else
    res = small * 10000000 + big * 10000 + product;
  return res;
}

int main() {
  int sum = 0;

  for (int small=1; small<100; small++) {
    int big = 10000/small;
    int product = small*big;
    while (product > 1000) {
      product = small*big;
      if (isPandigital(concat(small, big, product))) {
        cout << small << " * " << big << " = " << product << "\n";
        sum += product;
      }
      big--;
    }
  }
}
