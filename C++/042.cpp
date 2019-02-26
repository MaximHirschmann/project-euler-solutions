#include <iostream>

using namespace std;

int main() {
  // length of the words from 1-100
  // first 20 are given manually, the rest will be calculated
  int ones[100] = {0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8};
  // length of "forty" and etc.
  int tens[10] = {0,4,6,6,5,5,5,7,6,6};
  int result = 0;
  // 1-20
  for (auto i: ones) {
    result += i;
  }
  // 20-100
  for (int ten=2; ten<10; ten++) {
    for (int one=0; one<10; one++) {
      int length = tens[ten] + ones[one];
      ones[10*ten+one] = length;
      result += length;
    }
  }
  // 100-1000
  for (int i=100; i<1000; i++) {
    int last = result;
    int hundred = i/100;
    int rest = i%100;
    if (rest == 0)
      result += ones[hundred] + 7; // 7 becaufe of: "hundred"
    else
      result += ones[hundred] + 10 + ones[rest]; // 10 because of "hundred and"
  }
  cout << result + 11; // + "one thousand"
}
