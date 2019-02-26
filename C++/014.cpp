#include <iostream>

using namespace std;

int collatzLength(long long int n);

int collatzLength(long long int n) {
    int count = 0;
    while (1) {
      if (n == 1)
        return count + 1;
      if (n%2 == 0)
        n /= 2;
      else
        n = 3*n + 1;
      count++;
    }
}

int main() {
  int max = 0, index = 0;
  for (int i=1; i<1000000; i++) {
    int length = collatzLength(i);
    if (length > max) {
      max = length;
      index = i;
    }
  }
  cout << index << endl;
}
