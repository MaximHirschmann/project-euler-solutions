#include <iostream>
#include <unordered_map>

using namespace std;

int main() {
  unordered_map<int, int> table;
  for (int i=-199; i<201; i++)
    table[i] = 0;
  table[0] = 1;
  int coins[] = {1,2,5,10,20,50,100,200};

  for (auto coin:coins) {
    for (int amount=1; amount<201; amount++)
      table[amount] += table[amount-coin];
  }
  cout << table[200];
}
