#include <iostream>

using namespace std;

int main() {
  double product = 1.0;
  double n = 20;
  for (int i=1; i<=n; i++) {
    product *= ((n+i)/i);
  }
  cout.precision(100);
  cout << product << endl;
}
