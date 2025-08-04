# 四則演算関数

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError('0で割ることはできません')
    return a / b

if __name__ == "__main__":
    print("Hello World!")