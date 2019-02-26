#include <iostream>
#include "Utils.h"

using namespace std;

int main(){
  int limit = 2000000;
  bool nums[limit];
  sieve(limit, nums);
  long long int sum = 0;
  for (int i=0; i<limit; i++){
    if (nums[i])
      sum += i;
  }
  cout << sum;
}
