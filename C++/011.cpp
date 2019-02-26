#include <iostream>
#include <fstream>

using namespace std;

const int a = 20;
const int b = 20;
const int adjacent = 4;
int grid [a][b];

int max_grid();
int max_right();
int max_down();
int max_diagonal_left();
int max_diagonal_right();

int max_grid(){
  int maxs[4] = {
    max_right(),
    max_down(),
    max_diagonal_left(),
    max_diagonal_right(),
  };
  int max = 0;
  for (int i=0; i<sizeof(maxs)/sizeof(maxs[0]); i++) {
    if (maxs[i] > max) {
      max = maxs[i];
    }
  }
  return max;
}

int max_right(){
  int max = 0;
  for (int i=0; i<a; i++){
    for (int j=0; j<b-adjacent+1; j++){
      int prod = 1;
      for (int k=0; k<adjacent; k++) {
        prod *= grid[i][j+k];
      }
      if (prod > max)
        max = prod;
    }
  }
  return max;
}

int max_down() {
  int max = 0;
  for (int i=0; i<a-adjacent+1;i++) {
    for (int j=0; j<b; j++) {
      int prod = 1;
      for (int k=0; k<adjacent; k++) {
        prod *= grid[i+k][j];
      }
      if (max < prod)
        max = prod;
    }
  }
  return max;
}

int max_diagonal_left() {
  int max = 0;
  for (int i=adjacent-1; i<a-adjacent+1; i++) {
    for (int j=adjacent-1; j<b; j++) {
      int prod = 1;
      for (int k=0; k<adjacent; k++) {
        prod *= grid[i-k][j-k];
      }
      //cout << prod << endl;
      if (max < prod)
        max = prod;
    }
  }
  return max;
}

int max_diagonal_right() {
  int max = 0;
  for (int i=adjacent-1; i<a; i++) {
    for (int j=0; j<b-adjacent+1; j++) {
      int prod = 1;
      for (int k=0; k<adjacent; k++) {
        prod *= grid[i-k][j+k];
      }
      if (max < prod)
        max = prod;
    }
  }
  return max;
}

int main(){
  // build 2d array from 11.txt
  // set all values to 0
  for (int i=0; i<a; i++){
    for (int j=0; j<b; j++){
      grid[i][j] = 0;
    }
  }

  ifstream file;
  file.open("storage/11.txt");
  char c;
  int i = 0;
  int line = 0;
  while (file >> c){
    if ((int) c == 10){
      line++;
      i = 0;
    }
    else{
      if (i%2 == 0)
        grid[line][i/2] += (10*((int)c-48));
      else
        grid[line][i/2] += (int)c-48;
      i++;
    }
  }
  cout << max_grid();
}
