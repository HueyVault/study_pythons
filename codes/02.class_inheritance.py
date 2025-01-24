
# 기본 구조
# class class_name(parent_name) : 
#     variate
#     def __init__(self): 
#         pass
#


class Animal() :

    def __init__(self, name='JuJu'):
        self.name2 = name
        pass

    def speak(self, species):
        return f'{self.name2}는 {species} 종 입니다.'

class Dog(Animal) :
    def __init__(self):
        pass

    
class Cat(Animal) :
    def __init__(self, name='cat'):
        super().__init__(name)

    def walking(self, legs) :
        return f'{legs}로 걷는다.'
    
    def speak(self, species):
        return f'{species} species '


if __name__ == '__main__':
    # dog = Dog()
    cat = Cat()
    print(cat.speak('Cat'))
    print(cat.walking('네발'))

    pass
        
