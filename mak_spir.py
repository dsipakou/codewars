def spiral(size):
    direction = list(range(4))
    current_dir = 0
    stop = False
    output = [[0 for _ in range(size)] for _ in range(size)]
    i = 0
    j = 0
    changed_direction = False
    while not stop:
        output[i][j] = 1
        if current_dir == 0:
            print(i, j)
            if j < size - 2 and output[i][j + 2] != 1:
                changed_direction = False
                j += 1
 #           elif j < size - 1:
 #               changed_direction = False
 #               j += 1
            else:
                if changed_direction:
                    stop = True
                else:
                    current_dir = (current_dir + 1) % 4
                    changed_direction = True
        elif current_dir == 1:
            if i < size - 2 and output[i + 2][j] != 1:
                changed_direction = False
                i += 1
#            elif i < size - 1:
#                i += 1
            else:
                if changed_direction:
                    stop = True
                else:
                    current_dir = (current_dir + 1) % 4
                    changed_direction = True
        elif current_dir == 2:
            if j > 1 and output[i][j - 2] != 1:
                changed_direction = False
                j -= 1
 #           elif j > 0:
 #               j -= 1
            else:
                if changed_direction:
                    stop = True
                else:
                    current_dir = (current_dir + 1) % 4
                    changed_direction = True
        else:
            print(i, j)
            if i > 1 and output[i - 2][j] != 1:
                print(output[i - 2][j])
                changed_direction = False
                i -= 1
#            elif i > 0:
#                changed_direction = False
#                i -= 1
            else:
                print('else')
                if changed_direction:
                    stop = True
                else:
                    print('change', i, j)
                    current_dir = (current_dir + 1) % 4
                    changed_direction = True
    return output

def check_near(arr, i, j):
    pass

for i in spiral(10):
    print(i)
