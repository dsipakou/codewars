# subset array for storing permutations in the moment
subset = []

# output array for storing all permutations
output = []

# main function
def gen(k):
    if k == n + 1:
        print(subset)
        output.append(subset[:]) 
        return
    subset.append(k)
    gen(k + 1)
    subset.pop()
    gen(k + 1)

# permutations should start from 1 to n
n = 3
gen(1)
print(output)