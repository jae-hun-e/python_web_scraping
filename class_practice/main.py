
#! 객체지향 프로그래밍
class Car():
    # ! self는 호출한 instance 자신이다.
    def __init__(self, *arg, **args):
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.seats = 4
        self.color = args.get('color', 'black')
        self.price = args.get('price', '$20')

    # ! instance를print할때 자동으로 호출되서 str로 바꿔줌
    def __str__(self):
        return f'Car with doors : {self.doors} doors'


# ! 안에 숨겨져있는 method들을 알려준다.

print('car')
porche = Car(color='green', price="$40")
print(porche.color, porche.price)

mini = Car()
print(mini.color, mini.price)


# ! class 확장 (상속받기)
class Open_car(Car):

    def __init__(self, **kwargs):
        # ! super()는 부모의 속성,메서드를 사용하는 방법이다.
        # ! suoer().__init__(**kwargs)를 사용하면 부모의 init에 자식의**kwargs를 인자로 넣은 값을 가져올 수 있다.
        super().__init__(**kwargs)
        self.time = kwargs.get('zeroBack', 3)

    def __str__(self):
        return f"Car with no roof"

    def take_off(self):
        return 'taking off'


print('open_car')
bmw = Open_car(color='red')
print(bmw.color)
