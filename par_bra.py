def balanced_parens(n):
    output = []
    answ = solve(n, output)
    return list(filter(lambda item: item.count("(") == n, answ))
    
def solve(n, output = []):
    if n == 0:
        return [""]
    if n == 1:
        return ["()"]
    if n == 2:
        return ["()()", "(())"]
    for el in solve(n - 1):
        output.append("()" + el)
        output.append(el + "()")
        output.append("(" + el + ")")
    
    return list(set(output))

answer = balanced_parens(7)
print(answer)
print(len(answer))
answer = list(filter(lambda item: item.count("(") == 7, answer))
print(len(answer))