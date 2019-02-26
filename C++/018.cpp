#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {
  vector<vector<int>> pyramid;
  // build pyramid
  ifstream file;
  file.open("storage/18.txt");
  char c;
  int i = 0;  // index of row
  int j = 0;  // index of column
  bool k = true;  // if first(true) or second(false) digit of the number
  while (file >> noskipws >> c) {
    if ((int) c == 10) {  // new line
      i++;
      j = 0;
      k = true;
    }
    else if ((int) c == 32) { // whitespace
      j++;
      k = true;
    }
    else {
      if (j==0 & k) {
        vector<int> v(i+1);
        pyramid.push_back(v);
      }
      if (k)
        pyramid.at(i).at(j) += 10*((int) c - 48);
      else
        pyramid.at(i).at(j) += (int) c - 48;
      k = false;
    }
  }
  // algorithm
  for (int i=pyramid.size()-1; i>0; i--) {
    for (int j=0; j<pyramid.at(i-1).size(); j++) {
      if (pyramid.at(i).at(j) > pyramid.at(i).at(j+1))
        pyramid.at(i-1).at(j) += pyramid.at(i).at(j);
      else
        pyramid.at(i-1).at(j) += pyramid.at(i).at(j+1);
    }
  }

  cout << pyramid.at(0).at(0);
}
