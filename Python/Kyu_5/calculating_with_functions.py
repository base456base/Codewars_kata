"""
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3

Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby and Python)
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:
"""

def zero(n=''): return eval('0' + n)
def one(n=''): return eval('1' + n)
def two(n=''): return eval('2' + n)
def three(n=''): return eval('3' + n)
def four(n=''): return eval('4' + n)
def five(n=''): return eval('5' + n)
def six(n=''): return eval('6' + n)
def seven(n=''): return eval('7' + n)
def eight(n=''): return eval('8' + n)
def nine(n=''): return eval('9' + n)

def plus(n=''): return '+' + str(n)
def minus(n=''): return '-' + str(n)
def times(n=''): return '*' + str(n)
def divided_by(n=''): return '//' + str(n)

"""
the best
def zero(f = None): return 0 if not f else f(0)
def one(f = None): return 1 if not f else f(1)
def two(f = None): return 2 if not f else f(2)
def three(f = None): return 3 if not f else f(3)
def four(f = None): return 4 if not f else f(4)
def five(f = None): return 5 if not f else f(5)
def six(f = None): return 6 if not f else f(6)
def seven(f = None): return 7 if not f else f(7)
def eight(f = None): return 8 if not f else f(8)
def nine(f = None): return 9 if not f else f(9)

def plus(y): return lambda x: x+y
def minus(y): return lambda x: x-y
def times(y): return lambda  x: x*y
def divided_by(y): return lambda  x: x//y

"""