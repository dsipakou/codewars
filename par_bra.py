def balanced_parens(n):
    output = []
    return solve(n, output)
    
def solve(n, output):
    if n == 0:
        return [""]
    if n == 1:
        return ["()"]
    if n == 2:
        return ["()()", "(())"]
    for el in solve(n - 1, output):
        output.append("()" + el)
        output.append(el + "()")
        output.append("(" + el + ")")
    
    return list(set(output))


print(balanced_parens(4))