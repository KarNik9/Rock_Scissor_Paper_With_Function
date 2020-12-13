import random
import time

'''
TODO
########################################
########################################
print('комп выбрал ....')
if comp == 1:
    comp_choice = 'Камень'
elif comp == 2:
    comp_choice = 'Бугага'
elif comp == 3:
    comp_choice = 'Ножница'
    
print(f.renderText(comp_choice))


    '''



from pyfiglet import Figlet
f = Figlet(font='slant')
#1) функции, которые нам понадобятся
'''выбор_компьютера()
выбор_игрока()
возможные_варианты_выгриша()'''
#написать логические части программы

#3) описываем сами функции
'''a = 5
b = 10
def summa(slagaemoe1, slagaemo2):
    summa = slagaemo2 + slagaemoe1
    return summa
summa(a, b)'''

'''ПРИМЕР 
##############################
##############################
from random import randint
number = -1

def new_func(number):
    number = randint(1,3)
    return number

new_func(number)
print(number)
################################
################################'''

def computer_choice(global_comp):
    '''Принимает глобальную переменную comp и записывает в нее случайное число от одного до трех'''

    comp = random.randint(1,3)
    return comp

  
def choice_player(player_choice):
    x = int(input('ИГРОК1:  введите число: 1 - ножница , 2 - аминь, 3 - бумаги. \n'))
    while x > 3 or x < 1:  #зачем это нужно, Это нужно для того чтобы проверять выбор игрока не меньше ли он 1 или не больше 3
        print("НЕ ПРАВИЛЬНЫЙ ОТВЕТ!!!")
        x = int(input('Введите заново: 1,2 или 3! \n'))
    return x
  

def check_winner(x, comp):
    if x == 1 and comp == 2:
        print (f.renderText('The comp won! \n'))
    elif x == 2 and comp == 3:
        print (f.renderText('The comp won! \n'))
    elif x == 3 and comp == 1:
        print (f.renderText('The comp won! \n'))

    #случаи, когда выигрывает ИГРОК
    elif x == 2 and comp == 1:  
        print('Пользователь выбрал ', x, 'и выиграл! \n')
        print (f.renderText('The user  won! \n'))
    elif x == 3 and comp == 2:
        print('Пользователь выбрал', x, 'и выиграл! \n')
        print (f.renderText('The user  won! \n'))
    elif x == 1 and comp == 3:
        print('Пользователь выбрал', x, 'и выиграл! \n')
        print (f.renderText('The user  and won! \n'))
    else:
        print (f.renderText('Draw'))
    

'''################################
################################
Основная часть программы
################################
################################'''
################################################################################################################################################################################

x = 0
comp = 0
comp = computer_choice(comp)  #ВОТ ТУТ ПРИСВОИТСЯ СЛУЧАЙНОЕ ЗНАЧЕНИЕ ПЕРЕМЕННОЙ comp
x = choice_player(x)
print(comp)
check_winner(x,comp)



























































































