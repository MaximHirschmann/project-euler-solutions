#include <iostream>

using namespace std;

int main(){
  int limit = 100;
  int sum_of_squares = 0, square_of_sum = 0;
  for (int i=1; i<=limit; i++){
    sum_of_squares += i*i;
    square_of_sum += i;
  }
  square_of_sum *= square_of_sum;
  cout << square_of_sum-sum_of_squares;
}
