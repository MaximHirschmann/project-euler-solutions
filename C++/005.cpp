#include <cmath>
#include <iostream>
#include "Utils.h"

using namespace std;

int main(){
  int res = 1;
  int limit = 20;
  bool arr[limit];
  sieve(limit, arr);
  for (int i=0; i<limit; i++){
    if (arr[i]){ // if prime
      // get l where prime^l = limit and floor it
      int l = (int)(log(limit)/log(i));
      res =  res * round(pow(i, l));
    }
  }
  cout << res;
}
