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
  int size = 1;
  int a[200] = {1};
  int n = 100;
  for (int i=2; i<=n; i++) {
    size = multiply(i, a, size);
  }
  int res = 0;
  for (auto i: a) {
    res += i;
  }
  cout << res;
}
