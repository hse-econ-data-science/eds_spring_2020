# классы!

# создадим класс для комплексных чисел!
from numpy import sqrt, arctan2

class complex:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im
    def __repr__(self): # что-то максимально компактное
        return "complex(%r, %r)" % (self.re, self.im)
    def __str__(self): # более длинное человеческое описание
        if self.im >= 0:
            return "комплексное число %r + %r * i" % (self.re, self.im)
        return "комплексное число %r - %r * i" % (self.re, -self.im)
    def __add__(self, other):
        re = self.re + other.re
        im = self.im + other.im
        return complex(re, im)
    def __abs__(self):
        # длина комплексного числа как вектора на плоскости
        return sqrt(self.re ** 2 + self.im ** 2)
    def __rmul__(self, other):
        re = other * self.re
        im = other * self.im
        return complex(re, im)
    def __mul__(self, other):
        re = self.re * other.re - self.im * other.im
        im = self.re * other.im + self.im * other.re
        return complex(re, im)
    def quarter(self):
        if self.re > 0:
            if self.im > 0:
                return 1
            return 4
        if self.im > 0:
            return 2
        return 3
    def arg(self):
        return arctan2(self.im, self.re)


# тестирование класса 

z = complex(5, 6)
z

z.re
z.im

print(z)

w = complex(3, 4)
z + w
z * w
5 * z

"Привет, дорогой %r. У нас всё хорошо" % 4

abs(z)
z.quarter()

# упражнение 1:
# определите произведение двух комплексных чисел
# упражнение 2:
# метод, который выводит четверть плоскости (1, 2, 3, 4)
# в кот-ой лежит комплексное число
# для спорных ситуаций не важно

z += w

# упражнение 3.
# arg() угол с осью re (горизонтальная)
arctan2(1, 1)
3.14 / 4
arctan2(-1, -1)
z.arg()

# упражнение 4
a = complex(-5, -6)
print(a)
