subset = []
output = []

def gen(k):
    if k == n + 1:
        print(subset)
        output.append(subset[:]) 
        return
    subset.append(k)
    gen(k + 1)
    subset.pop()
    gen(k + 1)
n = 3
gen(1)
print(output)