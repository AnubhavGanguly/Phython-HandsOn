def add (a,b):
    return a+b
def subtraction (a,b):
    return a-b
def multiplication (a,b):
    return (a*b)

def divide(a,b):
    try:
        return a//b
    except ZeroDivisionError:
        return("Divisor can't ne zero.")