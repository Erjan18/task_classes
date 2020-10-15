class Fish:
    def __init__(self,types,scale,fins,gills,tooth):
        self.types = types
        self.scale = scale
        self.fins = fins
        self.gills = gills
        self.tooth = tooth
        self. energy = 100

    def type(self):
        return f'{self.types} {self.scale} {self.fins} {self.gills} {self.tooth}'


    def die(self,food):
        if food > 0:
            print('Наелся')
        else:
            print('умер от голода')

    def swim(self,km):
        res = km // 10
        self.energy -= res
        return res

class Fight:
    def kill(self,Whale,Shark):
        self.Whale = Whale
        self. Shark = Shark
        if Whale > Shark:
            print('Победил Синий кит')
        else:
            print('Победила Белая акула')

class White_Shark(Fish):

    def __init__(self,types,scale,fins,gills,tooth):
        super().__init__(types,scale,fins,gills,tooth)
        self.size = 6
        self.speed = 56
        self.terrible = True
        self.sharp_tooth = True
        self.very_hungry = True
        self.energy = 100

    def swim(self,km):
        res = km // 10
        self.energy -= res
        return res


    def eat(self,food):
        if food == 'fish':
            self.energy = self.energy + 20
            print(self.energy)
        elif food == 'tiger_shark':
            self.energy = self.energy + 50
            print(self.energy)
        elif food == 'human':
            self.energy = self.energy + 100
            print(self.energy)

class Blue_Whale(Fish):
    def __init__(self,types, scale, fins, gills, tooth):
        super().__init__(types,scale, fins, gills, tooth)
        self.types = types
        self.size = 25
        self.blowhole = True
        self.whalebone = True
        self.hungry = True
        self.energy = 100

    def type(self):
        return f'{self.types} {self.scale} {self.fins} {self.gills} {self.tooth}'

    def growth(self,food):
        if food == 'plankton':
            self.size = self.size + 1
            print(self.size)
        elif food == 'fish':
            self.size = self.size + 2
            print(self.size)
        elif food == 'shark':
            self.size = self.size + 3
            print(self.size)

shark = White_Shark('Белая акула','Кожа','Плавники','Жабры','Острые зубы')
print(shark.type())
shark.swim(100)
shark.eat('fish')
shark.energy = 100

whale = Blue_Whale ('Синий кит','Кожа','Плавники','Легкие','Китовый ус')
print(whale.type())
whale.growth('shark')
whale.size = 25

Whale = Fight()
Shark = Fight()
Whale.kill(500,300)
