
# 기본 구조
# class class_name(parent_name) : 
#     variate
#     def __init__(self): 
#         pass
#


class Animal() :

    def __init__(self):
        self.name2 = 'JuJu'
        pass

    def speak(self, species):
        return f'{self.name2}는 {species} 종 입니다.'






if __name__ == '__main__':
    animal = Animal()
    print(animal.speak('Cat'))
    pass
        
