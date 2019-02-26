#include "Utils.h"

using namespace std;

int main() {
  long long int max3 = 0, max4 = 0;

  for (int i=9999; i>=5000; i--) {
    if (i<=max4)
      break;
    long long int num = i*100000 + 2*i;
    if (isPandigital(num))
      max4 = i;
  }

  for (int i=333; i>=192; i--) {
    if (i <= max3)
      break;
    long long int num = i*1000000 + 2*i*1000 + 3*i;
    if (isPandigital(num))
      max3 = i;
  }

  if (max3 > max4)
    cout << max3*1000000 + 2*max3*1000 + 3*max3;
  else
    cout << max4*1000000 + 2*max4;
}
