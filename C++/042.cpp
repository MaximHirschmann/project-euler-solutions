#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <cmath>

using namespace std;

int nameScore(string s) {
  int sum = 0;
  for (auto c: s) {
    sum += (int) c - 64; // 64 because ascii of A = 65
  }
  return sum;
}

bool isPerfectSquare(int n) {
  int root = sqrt(n) + 0.5;
  return root*root == n;
}

bool isTriangleNumber(int n) {
  return isPerfectSquare(8*n+1);
}

bool isTriangleWord(string s) {
  return isTriangleNumber(nameScore(s));
}

int main() {
  vector<string> words;

  ifstream file;
  file.open("storage/42.txt");
  char c;
  string word = "";
  while (file >> c) {
    if ((int) c == 44) { // if "," begin new word
      words.push_back(word);
      word = "";
    }
    else if ((int) c != 34) { // if not " then add char to string
      word += c;
    }
  }

  int count = 0;

  for (auto s: words) {
      if (isTriangleWord(s))
        count += 1;
  }
  cout << count << "\n";
}
