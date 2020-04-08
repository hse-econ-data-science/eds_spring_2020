# классы в питоне!

kartoshka.jarit()
jarit(kartoshka)

# комплексные числа в виде класса
# a + b * i
# модуль комплексного числа \sqrt{a^2 + b^2}

from numpy import sqrt
from numpy import arctan2

class complex:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

    def __abs__(self):
        return sqrt(self.re ** 2 + self.im ** 2)
    
    def __add__(self, other): 
        re = self.re + other.re
        im = self.im + other.im
        return complex(re, im)

    def __mul__(self, other): 
        re = self.re * other.re - self.im * other.im
        im = self.re * other.im + self.im * other.re
        return complex(re, im)

    def __repr__(self):
        return "complex(%r, %r)" % (self.re, self.im)

    def __str__(self):
        if self.im >= 0:
            return "комплексное число %r + %r * i" % (self.re, self.im)
        return "комплексное число %r - %r * i" % (self.re, -self.im)

    def arg(self):
        return arctan2(self.im, self.re)
    
    def __iadd__(self, other): 
        re = self.re + other.re
        im = self.im + other.im
        return complex(re, im)

# заново определить класс
# заново создать z
# упражнение 1: реализуйте умножение комплексных чисел
# в чатике *
z = complex(1, 2)
w = complex(1, 3)
r = z * w
r.im
r.re
# упражнение 2: реализуйте arg
# угол от оси горизонтальной (re) до комплексного числа
z = complex(1, 2)
z.arg()
# hint: arctan2, atan2 из numpy
# упражнение 3: сделайте красивый вывод для случая отрицательной Im(z)

# упражнение 4: определите для комплексных чисел +=

# домашка для практики: решите семинар 4 на гитхабе в ipynb!

