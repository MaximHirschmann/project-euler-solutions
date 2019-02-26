#include <iostream>
#include <fstream>

using namespace std;

int main() {
  int digits[52] = {};
  ifstream file;
  file.open("storage/13.txt");
  char c;
  int i = 0;
  //written addition
  while (file >> c) {
    digits[i%50+2] += (int) c - 48;
    i++;
  }
  // eliminate digits >= 10 until none are left (3 times)
  for (int k=0; k<3; k++){
    for (int i=2; i<52; i++) {
      int hun = digits[i]/100;
      int ten = (digits[i]-(hun*100))/10;
      digits[i-2] += hun;
      digits[i-1] += ten;
      digits[i] = digits[i]%10;
    }
  }
  for (int i=0; i<10; i++) {
    cout << digits[i];
  }
}
