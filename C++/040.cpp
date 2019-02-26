#include <iostream>
#include <cmath>

using namespace std;

int lengthInt(int n){
  //number of digits of int
  return int(log(n)/log(10))+1;
}

int main() {
  short int a[100100] = {};
  int number = 1, index = 0;
  while (index <= 100000) {
    int length = lengthInt(number);
    // add number to array
    int copy = number;
    int i = 0;
    while (copy != 0) {
      int mod = copy%10;
      a[index + (length-i)] = mod;
      copy = (copy-mod)/10;
      i++;
    }
    index += length;
    number++;
  }

  cout << a[1]*a[10]*a[100]*a[1000]*a[10000]*a[100000];
}
