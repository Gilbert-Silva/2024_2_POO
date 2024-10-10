#include <iostream>
#include <math.h> 

using namespace std;

int main() {
  cout << "Digite a base e a altura do retângulo" << endl;
  double b, h; 
  cin >> b;
  cin >> h;
  double area = b * h;
  double perimetro = 2 * b + 2 * h;
  double diagonal = sqrt(b * b + h * h);
  cout << "Área = " << area << " - Perímetro = " <<  perimetro <<
          " - Diagonal = " << diagonal << endl;
  return 0;
}

