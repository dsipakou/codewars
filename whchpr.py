def squares_needed(grains):
    if grains == 0:
        return 0
    square = 1
    grains -= 1
    index = 1
    while grains > 0:
        square *= 2
        grains -= square
        index += 1
    return index

print(squares_needed(4))
