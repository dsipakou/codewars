from functools import reduce

def greatest_product(n):
    output = 0
    for i in range(len(n) - 4):
        current_product = reduce((lambda x, y: x * y), [int(c) for c in n[i:i+5]])
        output = max(output, current_product)
    return output
