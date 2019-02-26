#include <iostream>
#include <unordered_map>
#include <string>
#include <algorithm>
#include <bits/stdc++.h>
#include <cmath>

using namespace std;

unordered_map<string, int> table;

int sumDigitsPower(int n, int exp) {
  // int n to string
  stringstream out;
  out << n;
  string s = out.str();
  // sort string to check if it is in table
  sort(s.begin(), s.end());
  if (table.find(s) != table.end())
    return table[s];
  // calculate sum
  int sum = 0;
  for (auto i: s)
    sum += pow((int) i - 48, exp);
  table[s] = sum;
  return sum;
}

int main() {

  int sum = 0;
  for (int i=10; i<354294; i++) {
    //cout << i << ": " << sumDigitsPower(i, 5) << "\n";
    if (i == sumDigitsPower(i, 5))
      sum += i;
  }
  cout << sum;

}
