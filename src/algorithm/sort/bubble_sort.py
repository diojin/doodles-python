import testdata
import copy

source = copy.deepcopy(testdata.dataset1)
print("original set:\t", source)

def bubble_sort( source ):
    '''The original bubble sort'''
    for i in range(len(source)-1, 0, -1):
        for j in range(0, i):
            if source[j] > source[j+1] :
                source[j], source[j+1] = source[j+1], source[j]

def enhanced_bubble_sort(source):
    '''The enhanced bubble sort.
    
    By using upper and lower bound'''
    left = 0
    right = len(source)-1
    while ( left < right ):
        new_bound = left
        for i in range(left, right):
            if source[i] > source[i+1]:
                source[i], source[i+1] = source[i+1], source[i]
                new_bound = i
        right = new_bound
        new_bound = left
        for i in range(right, left, -1 ):
            if source[i] < source[i-1]:
                source[i], source[i-1] = source[i-1], source[i]
                new_bound = i
        left = new_bound
                
print(bubble_sort.__doc__)
bubble_sort(source)
print("after {}:\t{}".format(bubble_sort.__name__, source))  

source = copy.deepcopy(testdata.dataset1)
print("original set:\t", source)
enhanced_bubble_sort(source)
print("after {}:\t{}".format(enhanced_bubble_sort.__name__, source)) 

