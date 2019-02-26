#include <iostream>
#include "Utils.h"

int main(){
  int res = 0;
  int product;
  for (int i=999; i>99; i--){
    if (i*999 <= res){
      break;
    }
    for (int j=999; j>=i; j--){
      product = i*j;
      if (product<=res){
        break;
      }
      if (isPalindrom(product)){
        res = product;
      }
    }
  }
  cout << res;
}
