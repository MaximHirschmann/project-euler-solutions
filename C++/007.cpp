#include <iostream>
#include "Utils.h"

using namespace std;

int nthPrime(int n);

int main(){
  cout << nthPrime(10001) << endl;
}

int nthPrime(int n){
  int count = 0;
  int i = 0;
  while (1){
    if (isprime(i)){
      count++;
      if (count == n){
        return i;
      }
    }
    i++;
  }
}
