#include <iostream>
#include <iomanip>

using namespace std;

class Triangulo {
    public: // controlar a visibilidade dos membros
    double b = 0, h = 0;
    double calc_area() {
        return b * h / 2;
    }
};

int main() {
  Triangulo x;   // Triangulo x = new Triangulo();
  cout << x.b << " " << x.h << endl;
  cout << "Informe o valor da base: ";
  cin >> x.b;
  cout << "Informe o valor da altura: ";
  cin >> x.h;
  cout << fixed << setprecision(2);
  cout << "Área = " << x.calc_area() << endl;
}