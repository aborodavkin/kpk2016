import turtle
from math import sin

t = turtle.Turtle()
t.shape("turtle")
t.color("darkgreen", "yellow")
t.shapesize(2)
t.speed(15)


def main():
    t.penup()
    t.backward(250)    
    n = input()
#введённое число - строка. Предполагаем, что введено именно число
    length = len(n)# получаем длину строки
    a=[]# заводим пустой список
    for i in range(length):
        a.append(int(n[i]))# заполняем список числами, полученными из введенной строки
        if a[i] == 1:       # и печатаем их с помощью черепашки
            digit_one(50)
            t.forward(20)
        elif a[i] == 2:
            digit_two(50)
            t.forward(20)
        elif a[i] == 3:
            digit_three(50)
            t.forward(20)
        elif a[i] == 4:
            digit_four(50)
            t.forward(20)
        elif a[i] == 5:
            digit_five(50)
            t.forward(20)
        elif a[i] == 6:
            digit_six(50)
            t.forward(20)
        elif a[i] == 7:
            digit_seven(50)
            t.forward(20)
        elif a[i] == 8:
            digit_eight(50)
            t.forward(20)
        elif a[i] == 9:
            digit_nine(50)
            t.forward(20)
        elif a[i] == 0:
            digit_zero(50)
            t.forward(20)  
    t.hideturtle()

    

def digit_one(length):
    """ Рисует цифру с высотой length
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    t.penup()
    t.forward(length/2)
    t.pendown()
    t.left(90)
    t.forward(length)
    t.left(90+45)
    t.forward(length*sin(45*3.141592/180))
    #обратный ход
    t.backward(length*sin(45*3.141592/180))
    t.right(90+45)
    t.backward(length)
    t.right(90)
    t.penup()

def digit_two(length):
    """ Рисует цифру с высотой length
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    L1 = length/2
    L2 = (length/2)*2**0.5
    B = [180, -135, 45, 90]
    A = [ L1, L2, L1, L1]

    t.penup()
    t.forward(L1)
    t.pendown()
    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)
    t.penup()


def digit_three(length):
    """ Рисует цифру с высотой length
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    L1 = length/2
    L2 = (length/2)*2**0.5
    B = [45, -225, 225, -225]
    A = [ L2, L1, L2, L1]

    t.penup()    
    t.pendown()
    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)
    t.penup()
    t.forward(L1)


def digit_four(length):
    """ Рисует цифру с высотой length
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    L1 = length/2   
    B = [90, 0, 180, 270, 270]
    A = [L1, L1, L1, L1, L1]

    t.penup()
    t.forward(L1)
    t.pendown()
    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)
    t.penup()


def digit_five(length):
    """ Рисует цифру с высотой length
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    L1 = length/2  
    B = [0, 90, 90, 270, 270]
    A = [L1, L1, L1, L1, L1]
    t.penup()   
    t.pendown()
    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)
    t.penup()
    t.forward(L1)
  

def digit_six(length):
    """ Рисует цифру с высотой length
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    L1 = length/2
    L2 = (length/2)*2**0.5
    B = [0, 45, 90, 90, 90]
    A = [L2, L1, L1, L1, L1]

    t.penup()
    t.forward(L1)
    t.left(90)
    t.forward(2*L1)  
    t.right(-135)
    t.pendown()
    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght) 
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)
    t.penup()
    t.forward(L2)
    t.left(45)
    t.forward(L1)
    t.left(90)
    t.forward(L1)



def digit_seven(length):
    """ Рисует цифру с высотой length
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    L1 = length/2
    L2 = (length/2)*2**0.5
    B = [90, -45, 135]
    A = [L1, L2, L1]

    t.penup()   
    t.pendown()
    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)
    t.penup()
    t.forward(L1)



def digit_eight(length):
    """ Рисует цифру с высотой length
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    L1 = length/2    
    B = [0, 90, 90, 90, -90, -90, -90]
    A = [L1, L1, L1, L1, L1, L1, L1]

    t.penup()
    t.forward(L1)
    t.left(90)
    t.forward(L1)
    t.pendown()
    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)
    t.penup()
    t.left(180)
    t.forward(L1)
    t.left(90)   



def digit_nine(length):
    """ Рисует цифру с высотой length
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    L1 = length/2
    L2 = (length/2)*2**0.5
    B = [0, 90, 90, 90, -135]
    A = [L1, L1, L1, L1, L2]

    t.penup()
    t.forward(L1)
    t.left(90)
    t.forward(L1)
    t.pendown()
    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)
    t.penup()
    t.left(180)
    t.forward(L1)
    t.left(90)    


def digit_zero(length):
    """ Рисует цифру с высотой length
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    L1 = length/2    
    B = [0, 90, 90, 0, 90, 90]
    A = [L1, L1, L1, L1, L1, L1]

    t.penup()
    t.forward(L1)
    t.left(90)
    t.forward(L1)
    t.pendown()
    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)
    t.penup()
    t.left(180)
    t.forward(L1)
    t.left(90)

main()

#t.left(30)
#t.right(30)
#t.forward(200)
#t.backward(200)
#t.penup()
#t.pendown()
#t.begin_fill()
#t.end_fill()




