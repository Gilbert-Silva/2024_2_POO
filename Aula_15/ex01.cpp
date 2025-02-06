#include <iostream>
#include <chrono>

int main() {
    // Número de operações
    const int n = 1000000;

    // Iniciar o cronômetro
    auto start = std::chrono::high_resolution_clock::now();

    // Realizar operações de ponto flutuante
    for (int i = 0; i < n; ++i) {
        volatile double result = 3.14159 * 2.71828;  // Exemplo de operação
    }

    // Parar o cronômetro
    auto end = std::chrono::high_resolution_clock::now();

    // Calcular o tempo decorrido
    std::chrono::duration<double> duration = end - start;
    
    // Calcular operações por segundo
    double operations_per_second = n / duration.count();

    std::cout << "Operações por segundo: " << operations_per_second << std::endl;

    return 0;
}
