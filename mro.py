### METHOD RESOLUTION ORDER ###

"""
  Es la forma en como python ejecuta un metodo de una clase cuando
  las clases la cual hereda tienen el mismo metodo
"""
class C():
    def method(self):
        print("C method")
class F(C):
    def method(self):
        print("B method")
class A(F):
    def method(self):
        print("A method")


class B(A):
    def method(self):
        print("B method")


class D(B, C):
    pass

d = D()
d.method()

print(D.__mro__)
