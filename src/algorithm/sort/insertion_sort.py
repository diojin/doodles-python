import testdata
import copy

source = copy.deepcopy(testdata.dataset1)
print("original set:\t", source)

def insertion_sort(source):
    """The original insertion sort."""
    for i in range(1, len(source)):
        tmp = source[i]
        j = i
        while ( j > 0 ) and source[j-1] > tmp:
            source[j] = source[j-1]
            j -= 1
        source[j] = tmp 

print(insertion_sort.__doc__)
insertion_sort(source)

print("after sort:\t", source)  

