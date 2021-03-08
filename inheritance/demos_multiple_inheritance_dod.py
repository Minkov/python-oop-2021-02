class GP:
    def f(self):
        print('GP')


class P1(GP):
    def f(self):
        print('P1')


class P2(GP):
    def f(self):
        print('P2')


class A(GP):
    def f(self):
        print('A')
        super().f()


print(A.mro())
A().f()
