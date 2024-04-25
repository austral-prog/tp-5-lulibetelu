def roots(a, b, c):
    discriminante = b**2-4*a*c
    if discriminante > 0:
        r1 = (-b + (discriminante)**(1/2))/(2*a)
        r2 = (-b - (discriminante)**(1/2))/(2*a)
        return f"({r1}, {r2})"
    elif discriminante == 0:
        r3 = ((-b)/(2*a))
        return f"({r3})"
    else:
        return "( )"
 

def value_y(a, b, c, x):
    y = a*(x**2) + b*x + c
    return float(f"{y}")

def to_string(a, b, c):
    if a != 0 and b!=0 and c!=0:
        return f"f(x) = {a} * X^2 + {b} * X + {c}"    
    elif a == 0 and b != 0 and c != 0:
        return f"f(x) = {b} * X + {c}"
    elif b == 0 and a != 0 and c != 0:
        return f"f(x) = {a} * X^2 + {c}"
    elif c == 0 and b != 0 and c != 0:
        return f"f(x) = {a} * X^2 + {b} * X"
    elif a == 0 and b == 0 and c != 0:
        return f"f(x) = {c}"
    elif a == 0 and c == 0 and b != 0:
        return f"f(x) = {b} * X"
    elif b == 0 and c == 0 and a != 0:
        return f"f(x) = {a} * X^2 "
    elif a == 0 and b == 0 and c == 0:
        return f"f(x) = 0"

def derivation(a, b, c):
    if a != 0 and b != 0:
        return f"f'(x) = {a*2} * X + {b}"
    elif a == 0 and b != 0:
        return f"f'(x) = {b}"
    elif b == 0 and a != 0:
        return f"f'(x) = {a*2} * X"
    elif a == 0 and b == 0:
        return f"f'(x) = 0"



