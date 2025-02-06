import time

# Número de operações
n = 1000000

# Medir o tempo de execução de operações de ponto flutuante
start_time = time.time()

# Realizar operações de ponto flutuante
for i in range(n):
    _ = 3.14159 * 2.71828  # Exemplo de operação

end_time = time.time()

# Calcular operações por segundo
elapsed_time = end_time - start_time
operations_per_second = n / elapsed_time

print(f"Operações por segundo: {operations_per_second:.2f}")
