# lamda function
first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda first1, second1: [first1[i] == second1[i] for i in range(len(first1))], first, second)))


# Замыкание
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        file = open(file_name, "w", encoding= "UTF - 8")
        for i in data_set:
            file.write(f"{i}\n")
        file.close()
    return  write_everything





write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# __call__
from random import choice
class MysticBall:
    def __init__(self,*words):
        self.word = words
    def __call__(self):
        return choice(self.word)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())


