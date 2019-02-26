#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <algorithm>

using namespace std;

int nameScore(string name, int index) {
  int sum = 0;
  for (char c: name) {
    sum += (int) c - 64;
  }
  return sum * (index+1);
}

int main() {
  vector<string> names;

  ifstream file;
  file.open("storage/22.txt");
  char c;
  string name = "";
  while (file >> c) {
    if ((int) c == 44) { // if "," begin new word
      names.push_back(name);
      name = "";
    }
    else if ((int) c != 34) { // if not " then add char to string
      name += c;
    }
  }

  sort(names.begin(), names.end());

  int sum = 0;
  for (int i=0; i<names.size(); i++) {
    sum += nameScore(names.at(i), i);
  }
  cout << sum;
}
