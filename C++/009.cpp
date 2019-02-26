#include <cmath>
#include <iostream>
#include <vector>
#include "Utils.h"

using namespace std;

void triplets(int s, vector<vector<int>> & sol);

int main(){
  int s = 1000;
  vector<vector<int>> sol;
  triplets(s, sol);
  for (int i=0; i<sol.size(); i++){
    int prod = 1;
    for (int j=0; j<3; j++){
      prod *= sol.at(i).at(j);
    }
    cout << prod << endl;
  }
}
