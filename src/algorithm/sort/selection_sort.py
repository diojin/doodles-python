
import testdata
import copy

source = copy.deepcopy(testdata.dataset1)
print("original set:\t", source)

def selection_sort( source ):
    '''The "original" selection sort'''
    for i in range(len(source)-1, 0, -1):
        max = 0
        for j in range(1, i+1):
            # use >= instead of > to improve stability
            if source[j] >= source[max] :
                max = j
        # don't swap with itself
        if max != i:
            source[max], source[i]=source[i], source[max]

print(selection_sort.__doc__)
selection_sort(source)
print("after {}:\t{}".format(selection_sort.__name__, source))  

