#include <iostream>

using namespace std;

bool isDivisible(char d[9]) {
  if (d[0] == 0) {
    return false;
  }
  char divisors[] = {2,3,5,7,11,13,17};
  for (int i=0; i<7; i++) {
    if ((d[i+1]*100 + d[i+2]*10 + d[i+3]) % divisors[i] != 0)
      cout << d[i+1]*100 + d[i+2]*10 + d[i+3] << " % " << divisors[i] << " = " << (d[i+1]*100 + d[i+2]*10 + d[i+3]) % divisors[i] != 0 << "\n";
      return false;
  }
  return true;
}

int main() {
  char digits = {1,4,0,6,3,5,7,2,8,9};

}
