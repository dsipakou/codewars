def quickSort(array):
    return main_job(array, 0, len(array)-1)

def main_job(array, start, end):
    print(start, end)
    if start > end:
    	return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
    	if array[left] >= array[pivot] and array[right] < array[pivot]:
    		array[left], array[right] = array[right], array[left]
    	if array[left] < array[pivot]:
    		left += 1
    	if array[right] >= array[pivot]:
    		right -=1
    array[pivot], array[right] = array[right], array[pivot]
    main_job(array, start, right - 1)
    main_job(array, right + 1, end)
    return array
print(quickSort([6,5,7,5,4,23,2]))
