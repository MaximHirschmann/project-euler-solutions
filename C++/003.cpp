#include <iostream>
#include "Utils.h"
#include <vector>

int main(){
  vector<long long int> factors;
  primefactors(600851475143, factors);
  for (int i=0; i<factors.size();i++){
    std::cout << factors.at(i) << std::endl;
  }
  return 0;
}
