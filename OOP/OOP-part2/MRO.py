
# Method Resolution Order

class A:
    pass
    # def do_something(self):
    #     print("Method Define in : A")

class B(A):
    pass
    # def do_something(self):
    #     print("Method Define in : B")
class C(A):
    pass
    # def do_something(self):
    #     print("Method Define in : C")
class D(B,C):
    pass
    # def do_something(self):
    #     print("Method Define in : D")

# print(D.__mro__)
# print(D.mro())
# print(help(D))

thing = D()
thing.do_something()
