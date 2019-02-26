#include "Utils.h"
#include <algorithm>

using namespace std;


int main() {
  vector<char> v = {'1','2','3','4','5','6','7','8','9'};
  char digits[9];

  for (int i=0; i<8; i++) {
    for (int j=0; j<9-i; j++)
      digits[j] = v.at(j);

    for (int j=0; j<factorial(9-i);j++) {
      prev_permutation(digits, digits+9-i);
      
      long long int test = stoi(digits, 9-i);
      cout << test << "\n";
    }
  }
}
