# 데이터 속성(field) 상속

class A:
    def __init__(self):
        print("A.__init__()")
        self.message ="Hello"

class B(A):
    def __init__(self):
        print("B.__init__()")

if __name__ == "__main__":
    obj = B()

    print(obj.message)
