
import testdata
import copy

source = copy.deepcopy(testdata.dataset1)
print("original set:\t", source)

# need to be very careful with array index boundary, 
# since negtive index is meaningful.
def quick_sort(source, start, end):
    '''Quick sort algorithm'''
    if start < end:
        target = start
        left = start
        right = end+1
        while left < right :
            left += 1
            while left < right and source[left] <= source[target]:
                left += 1

            right -= 1
            while right >= left and source[right] >= source[target]:
                right -= 1

            if left < right:
                source[left], source[right] = source[right], source[left]

        source[target], source[right] = source[right], source[target]
        quick_sort(source,start,right-1)
        quick_sort(source,right+1, end)        

print(quick_sort.__doc__)
quick_sort(source, 0, len(source)-1)
print("after {}:\t{}".format(quick_sort.__name__, source))  

