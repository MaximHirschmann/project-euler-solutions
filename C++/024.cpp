#include <iostream>
#include <algorithm>

using namespace std;

int main() {
  char digits[] = {'0','1','2','3','4','5','6','7','8','9'};
  int len = sizeof(digits)/sizeof(digits[0]);
  for (int i=0; i<=1000000; i++) {
    next_permutation(digits, digits+len);
  };
  cout << digits;
}
