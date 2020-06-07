class A:
    def __init__(self):
        print("Init A")


class B:
    def __init__(self):
        print("Init B")
        # super().__init__()


class C(B, A):
    def __init__(self):
        print("Init C")
        super().__init__()
        super().__init__()


c = C()
