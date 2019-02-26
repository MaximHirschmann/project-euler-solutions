#include "Utils.h"
#include <unordered_map>

using namespace std;

int triangleNumber(int n);

unordered_map<int, int> table = {{0,0}};

int triangleNumber(int n) {
    if (table.find(n) != table.end())
      return table[n];
    else {
      int number = triangleNumber(n-1) + n;
      table[n] = number;
      return number;
    }
}

int main() {
  int i = 1;
  while (1) {
    int n = triangleNumber(i);
    if (divisorFuntion(n) > 500) {
      cout << n;
      break;
    }
    i++;
  }
}
