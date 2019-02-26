#include <iostream>

using namespace std;

int multiply(int n, int a[], int size);

int multiply(int n, int a[], int size) {
  int carry=0,i,p;

	for(i=0; i<size; i++) {
		p = a[i]*n+carry;
		a[i] = p%10;
		carry = p/10;
	}

	while(carry != 0) {
		a[size]=carry%10;
		carry=carry/10;
		size++;
	}
  return size;
}

int main() {
  int a[400] = {1};
  for (int i=0; i<1000; i++) {
    multiply(2, a, 400);
  }
  int sum = 0;
  for (auto i: a) {
    sum += i;
  }
  cout << sum;
}
