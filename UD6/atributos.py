

class Datos :

    i = 5
    x = 10

a = Datos()
print (a.i)
print (a.x)

class Metodo :
    def f(self):
        return "hello world"

a = Metodo()
print(a.f())
b = a.f()
print(b)

class Coche:
    marca = "Toyota"
    def __init__(self, modelo):
        self.modelo = modelo

a = Coche("Corola")
print(a.modelo)
print(a.marca)
