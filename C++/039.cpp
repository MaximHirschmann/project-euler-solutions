#include <iostream>
#include <cmath>

using namespace std;

int sidesWithPerimeter(int p) {
  int count = 0, a = 1;
  float b = 2.0;
  while (a<b) {
    b = (2.0*a*p - p*p)/(2*a-2*p);
    if (abs(b-round(b)) < 0.0001)
      count++;
    a++;
  }
  return count;
}

int main() {
  int maxLength=0, maxIndex=0;
  for (int i=12; i<1001; i++) {
    int length = sidesWithPerimeter(i);
    if (length>maxLength) {
      maxLength = length;
      maxIndex = i;
    }
  }
  cout << maxIndex;
}
