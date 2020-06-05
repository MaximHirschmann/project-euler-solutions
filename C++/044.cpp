#include <iostream>
#include "Utils.h"

int main() {
  for (int i=0; i<100; i++) {
    cout << i << ": " << pentagonalNumber(i)
    << ", " << isPentagonalNumber(pentagonalNumber(i)) << "\n";

  }

}
