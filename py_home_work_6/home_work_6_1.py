value = 7

def multi():
    global value
    value = value * 4
    print("Value in function:", value)

multi()
print("Value outside the function:", value)
