#include <iostream>

using namespace std;

int main() {
  int x = 10;   // variável estática
  int* y = &x;
  cout << x << endl;
  cout << &x << endl;
  cout << y << endl;
  cout << &y << endl;
  cout << *y << endl;
  y = new int();  // variável dinâmica
  cout << y << endl;
  *y = 20;
  cout << x + (*y) << endl;
  delete y;
}   
