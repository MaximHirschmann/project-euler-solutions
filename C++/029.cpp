#include <iostream>
#include <cmath>
#include "Utils.h"

using namespace std;


int main() {
  int limit = 100;
  int res = (limit-1) * (limit-1);

  int base = 2;

  while (base*base <= limit) {
    if (!isPerfectPower(base)) {
      int max_exp = log(limit)/log(base);
      for (int exp=2; exp<limit*(max_exp-1)+1; exp++) {
        bool substract = exp <= limit;
        for (int d=2; d<max_exp+1; d++) {
          if (exp%d == 0) {
            int new_exp = exp/d;
            if (new_exp != 1 & new_exp <= limit) {
              if (substract)
                res--;
              else
                substract = true;
            }
          }
        }
      }
    }
    base++;
  }
  cout << res << "\n";
}
