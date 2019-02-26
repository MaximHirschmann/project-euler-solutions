#include "Utils.h"

using namespace std;

int main() {
  int numerator = 1, denominator = 1;
  for (int cancel=1; cancel<10; cancel++) {
    for (int i=1; i<10; i++) {
      for (int j=1; j<10; j++) {
        int num = 10*i + cancel;
        int denom = 10*cancel + j;
        float fract = (num*1.0)/denom;
        float simple = (i*1.0)/j;
        if (fract < 1 & fract == simple) {
          numerator *= num;
          denominator *= denom;
        }
      }
    }
  }
  cout << numerator << ", " << denominator;
  int result = denominator / gcd(numerator, denominator);
  cout << result;
}
