#include <iostream>
#include <string>

using namespace std;

string add(string a, string b) {
  // a >= b
  int len = a.length();
  // make a and b the same length
  for (int i=0; i<len-b.length(); i++)
    b += '0';
  string res;
  int temp = 0;
  // written addition
  for (int i=0; i<len; i++) {
    int added = (int) a[i] + (int) b[i] + temp - 96;
    temp = added/10;
    res += (char) ((added%10)+48);
  }
  if (temp)
    res += (char) (temp+48);
  return res;
}

int main() {
  int count = 2;
  string lastlast = "1";
  string last = "1";
  while (last.length() < 1000) {
    string res = add(last, lastlast);
    lastlast = last;
    last = res;
    count++;
  }
  cout << count;
}
