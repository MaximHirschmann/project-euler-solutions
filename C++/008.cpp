#include <iostream>
#include <fstream>

using namespace std;

int main(){
  int adjacent = 13;
  int length = 1000;
  long long max = 0;
  char nums[length];
  ifstream file;
  file.open("storage/8.txt");
  file >> nums;
  for (int i=0; i<length-adjacent; i++){
    long long int prod = 1;
    for (int j=0; j<adjacent; j++){
      prod *= (nums[i+j]-48);
    }
    if (prod > max){
      max = prod;
    }
  }
  cout << max;
}
