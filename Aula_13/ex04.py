try:
    a = int(input("Informe o dividendo: "))
    b = int(input("Informe o divisor: "))
    print(a/b)
except ValueError as erro:
    print(erro)
finally:
    print("Ok")
print("Fim")