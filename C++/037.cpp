#include "Utils.h"

using namespace std;

bool isLeftTruncatablePrime(string s) {
  int len = s.size();
  for (int trash=0; trash<len-1; trash++) {
    s = s.substr(1, s.size()-1); // remove left digit
    if (!isprime(stoi(s))) {
      return false;
    }
  }
  return true;
}

int main() {
  string primes[] = {"2", "3", "5", "7"};
  char add[] = {'1','3','7','9'};
  vector<string> products;
  for (auto i: primes) {
    for (auto j: add)
      products.push_back(i+j);
  }
  vector<string> candidates;

  for (int trash=0; trash<7; trash++) {
    for (int i=products.size()-1; i>=0; i--) {
      if (!isprime(stoi(products[i]))) {
        products.erase(products.begin()+i);
      }
    }
    for (auto i: products)
      cout << i << ", ";
    cout << "\n\n";

    candidates.insert(candidates.end(), products.begin(), products.end());
    vector<string> replacement;
    for (auto i: products) {
      for (auto j: add) {
        replacement.push_back(i+j);
      }
    }
    products = replacement;
  }

  int sum = 0;
  for (auto i: candidates) {
    if (isLeftTruncatablePrime(i)) {
      sum += stoi(i);
    }

  }
  cout <<  "\n\n\n" << sum;
}
