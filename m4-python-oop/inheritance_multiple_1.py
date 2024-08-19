class A:
    def __init__(self):
        print("I belong to class A")
    def a_method(self):
        print("Inherited method from A")

class B:
    def __init__(self):
        print("I belong to class B")
    def b_method(self):
        print("Inherited method from B")

class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
    def c_method(self):
        print("method from C")

c_object = C()
c_object.a_method()
c_object.b_method()
c_object.c_method()