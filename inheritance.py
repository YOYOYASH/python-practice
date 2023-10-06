class A:
    def __init__(self):
        print("init of A")


class B(A):
    def __init__(self):
        super().__init__()
        print("init of B")


b1 = B()
