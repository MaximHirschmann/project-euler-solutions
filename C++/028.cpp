#include <iostream>
#include <unordered_map>

using namespace std;

unordered_map<int, int> table;

int spiral(int n) {
  if (table.count(n) != 0)
    return table[n];
  int res = spiral(n-1) + 2*((n-1)/4) + 2;
  table[n] = res;
  return res;
}

int main() {
  table[0] = 1;
  int d = 1001;
  int sum = 0;
  for (int i=0; i<2*d-1; i++)
    sum += spiral(i);
  cout << sum;
}
