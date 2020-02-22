def man(arr):
    men = []
    boys = []
    for item in arr:
        if item % 2 == 0:
            men.append(item)
        else:
            boys.append(item)
    men.sort()
    boys.sort(reverse=True)
    return men + boys

print(man([82,91,72,76,76,100,85]))
