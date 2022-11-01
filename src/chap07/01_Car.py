class Car:
    def __init__(self):
        self.color = 0xFF0000  # 차량 색상(빨강)
        self.wheel_size = 16 # 바퀴의 크기
        self.displacement = 2000 # 엔진 배기량

    def forward(self):    # 전진
        pass

    def backward(self):    # 후진
        pass

    def turn_left(self):    # 좌회전
        pass
    
    def turn_right(self):    # 우회전
        pass
    

if __name__ == "__main__":
    my_car = Car()

