
# 1
def add(x):
    return x+x

# 2
def sub(x):
    return x-x

# 3
def mul(x):
    return x*x

# 4
def div(x):
    return x/x


n = 4

fn = [add, sub, mul, div][n-1]

print(fn(3))