#include <iostream>

using namespace std;

int main() {
  int res = 0;
  int lengths[12] = {31,31,28,31,30,31,30,31,31,30,31,30};
  int day = 5;
  for (int year=1901; year<2001; year++) {
    for (int month=0; month<12; month++) {
      int days = lengths[month];
      if (month == 2 and year%4 == 0)
        days += 1;
      day = (day+days)%7;
      if (day == 6) {
        res += 1;
      }
    }
  }
  cout << res;
}
