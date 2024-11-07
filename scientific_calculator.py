import math

def sin(angle):
    if not isinstance(angle, (int, float)):
        raise TypeError("Input have to be numeric!")
    return math.sin(math.radians(angle))

def cos(angle):
    if not isinstance(angle, (int, float)):
        raise TypeError("Input have to be numeric!")
    return math.cos(math.radians(angle))

def tan(angle):
    if not isinstance(angle, (int, float)):
        raise TypeError("Input have to be numeric!")
    return math.tan(math.radians(angle))

def sqrt(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Input have to be numeric!")
    if value < 0:
        raise ValueError("Cannot take sqrt of negative number")
    return math.sqrt(value)

def log(value, base):
    if not isinstance(value, (int, float)):
        raise TypeError("Input have to be numeric!")
    if value <= 0:
        raise ValueError("Undefined for Values less than or equal to 0")
    return math.log(value, base)

def exp(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Input have to be numeric!")
    return math.exp(value)

def asin(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input have to be numeric!")
    if x < -1 or x > 1:
        raise ValueError("Math error")
    return round(math.asin(x), 5) 

def acos(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input have to be numeric!")
    if x < -1 or x > 1:
        raise ValueError("Math error")
    return round(math.acos(x), 5)  

def atan(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input have to be numeric!")
    return round(math.atan(x), 5)  

def sinh(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input have to be numeric!")
    return round(math.sinh(x), 5) 

def cosh(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input have to be numeric!")
    return round(math.cosh(x), 5) 

def tanh(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input have to be numeric!")
    return round(math.tanh(x), 5) 
