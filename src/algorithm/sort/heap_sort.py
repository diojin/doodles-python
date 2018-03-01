import testdata
import copy
import math

source = copy.deepcopy(testdata.dataset1)
print("original set:\t", source)

def restore_recursive(source,startIdx, endIdx):
    '''Restore a group of complete binary trees except for the start node.
    
    This is for big-top heap, use recursive algorithm'''
    maxIdx = -1
    leftChild = startIdx * 2 + 1
    rightChild = leftChild + 1
    if leftChild <= endIdx:
        maxIdx = leftChild
    if rightChild + 1 <= endIdx and source[rightChild] > source[maxIdx]:
        maxIdx = rightChild
    if maxIdx != -1 and source[startIdx] < source[maxIdx]:
        source[maxIdx], source[startIdx] = source[startIdx], source[maxIdx]
        restore(source, maxIdx, endIdx)

def restore(source,startIdx, endIdx):
    '''Restore a group of complete binary trees except for the start node.
    
    This is for big-top heap.'''
    while startIdx <= math.floor((endIdx - 1)/2):
        maxIdx = 2 * startIdx + 1
        rightChild = maxIdx + 1
        if rightChild <= endIdx and source[rightChild] > source[maxIdx]:
            maxIdx = rightChild
        if source[maxIdx] > source[startIdx]:
            source[maxIdx], source[startIdx] = source[startIdx], source[maxIdx]
            startIdx = maxIdx
        else:
            break

def heap_sort( source ):
    '''The heap sort.
    
    This is for big-top heap'''
    print("Phrase 1: initially creating the heap")
    for i in range(math.floor((len(source)-2)/2), -1, -1):
        restore(source, i, len(source)-1)
    
    print("Phrase 2: swap and sort")
    for i in range(len(source)-1, 0, -1):
        source[0], source[i] = source[i], source[0]
        restore(source, 0, i-1)

print(heap_sort.__doc__)
heap_sort(source)
print("after {}:\t{}".format(heap_sort.__name__, source))  

