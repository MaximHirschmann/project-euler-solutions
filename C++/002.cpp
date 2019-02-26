#include <iostream>
#include <unordered_map>
#include <cmath>

int fib(int k);
std::unordered_map<int, int> nums;

int main(){
  nums[0] = 1;
  nums[1] = 1;
  int sum = 0, value = 1, i = 1;
  while (value < 4000000){
    if (std::fmod(value, 2.0) == 0){
      sum += value;
    }
    i++;
    value = fib(i);
  }
  std::cout << sum;
}

int fib(int k){
  if (nums.find(k) != nums.end()){
    return nums[k];
  }
  int res = fib(k-1) + fib(k-2);
  nums[k] = res;
  return res;
}
