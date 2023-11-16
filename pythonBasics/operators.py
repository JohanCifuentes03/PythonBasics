"""
**      Exponent                            2 ** 3      8
%       Modulus/remainder                   22 % 8      6
//      Integer division/floored quotient   22 // 8     2
/       Division                            22 / 8      2.75
*       Multiplication                      3 * 5       15
-       Subtraction                         5 - 2       3
+       Addition                            2 + 2       4
"""


# Some examples of use

def sum_number(a, b):
    return a + b


def exp_number(a, b):
    return a ** b


def divide_number(a, b):
    return a / b


def mult_number(a, b):
    return a * b


a = 10
b = 20

print(sum_number(a, b))
print(exp_number(a, b))
print(divide_number(a, b))
print(mult_number(a, b))
