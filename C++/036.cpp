#include "Utils.h"

int main() {
  int sum = 0;
  for (int i=1; i<1000000; i++) {
    if (isPalindrom(i)) {
      if (isPalindrom(fromDez(i, 2)))
      sum += i;
    }
  }
  cout << sum;
}
