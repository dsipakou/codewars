def odd_eve(arr):
    return 'even' if sum(arr) % 2 == 0 else 'odd'

print(odd_eve([0, 1, 2]))
