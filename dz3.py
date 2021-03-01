# 1)
# создать класс Human(имя и возраст)
# и два класса Prince и Cinderella которые наследуются от Human
# у принца должен быть размер туфельки и  метод который принимает лист золушек и выводит какой золушки подошла туфелька

class Human:

    def __init__(self, name, age):
        self.name = name
        self.age = age

class Prince(Human):

    def __init__(self, name: str, age: int, size_shoes: int ,madams:list ):
        super().__init__(name, age)
        self.size_shoes = size_shoes
        self.age = age
        self.name = name
        self.madams = madams

    def find_madam(self):
        for madam in self.madams:
            if madam['size_shoes'] == self.size_shoes:
                return f"попелюшка знайшлась це :{madam['name']}"



class Cinderella(Human):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.name = name
        self.age = age


list_cinderella= [
    {"name":"sveta","age":24,"size_shoes":38},
    {"name": "anna", "age": 15, "size_shoes": 28},
    {"name": "natasha", "age": 34, "size_shoes": 38},
    {"name": "karina", "age": 44, "size_shoes": 39},
    {"name": "dasha", "age": 23, "size_shoes": 35},
    {"name": "maryana", "age": 21, "size_shoes": 42},
    {"name": "uliana", "age": 20, "size_shoes": 36}
]
human = Human("Sergiy", 24)
prince = Prince("Taras",23, 35,list_cinderella)
print(prince.find_madam())

# 2)
# Создать класс Rectangle:
# -конструктор принимает две стороны x,y
# -описать арифметические методы:
#   + сума площадей двух экземпляров класса
#   - разница площадей
#   == или площади равны
#   != не равны
#   >, < меньше или больше
#   при вызове метода len() подсчитывать сумму сторон

class Rectangle:

    def __init__(self,x ,y):
        self.y = y
        self.x = x

    def plus(self):
        return self.x+self.y

    def minus(self):
        return self.x -self.y


    def dorivnue(self):
        if self.x == selfy:
            return f"{self.x} = {self.y}"

    def ne_dorivnue(self):
        if self.x != selfy:
            return f"{self.x} != {self.y}"

    def menshe(self):
        if self.x < self.y:
            return f"{self.x} менше за {self.y}"
        elif self.x > self.y:
            return f"{self.x} більше за {self.y}"

    def len(self):
      return  self.x+self.y


tests = Rectangle(21,21)
print(tests.plus())
tests2 = Rectangle(21,21)
print(tests.len())