import math


    # ── Binary operations (require a and b) ──────────────────────────────────

def add( a:int, b:int)->int:
    return a + b

def subtract( a:int, b:int)->int :
    return a - b

def multiply( a:int, b:int)->int :
    return a * b

def divide(a:int, b:int)->int :
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

