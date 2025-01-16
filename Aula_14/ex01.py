class Funcionario:
    def __init__(self, nome, salario_base):
        self.__nome = nome
        self._salario_base = salario_base
    def get_nome(self):
        return self.__nome
    def get_salario(self):
        return self._salario_base
    def __str__(self):
        return f"{self.__nome}, {self.get_salario()}"

class Gerente(Funcionario):
    def __init__(self, nome, salario_base, gratificacao):
        super().__init__(nome, salario_base)
        self.__gratificacao = gratificacao
    def get_salario(self):
        #return self._salario_base + self.__gratificacao
        return super().get_salario() + self.__gratificacao

x = Funcionario("José Maria", 5000)
y = Gerente("Maria José", 5000, 3000)
print(x.get_nome())
print(x.get_salario())
print(x)
print(type(x))
print(isinstance(x, object))
print(isinstance(x, Funcionario))
print(isinstance(x, Gerente))
print(y.get_nome())
print(y.get_salario())
print(y)
print(type(y))
print(isinstance(y, object))
print(isinstance(y, Funcionario))
print(isinstance(y, Gerente))

         