def man(arr):
    men = set()
    boys = set()
    for item in arr:
        if item % 2 == 0:
            men.add(item)
        else:
            boys.add(item)
    men = sorted(men)
    boys = sorted(boys, reverse=True)
    return men + boys

print(man([82,91,72,76,76,100,85]))
