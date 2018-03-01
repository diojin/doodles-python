import testdata
import copy

def merge(source, start, mid, end, target):
    '''Merge two disjoint parts of source array to target array'''    
    i = start
    j = mid
    targetIdx = start
    while i < mid or j <= end:
        # if the condition is changed to i < mid and ( source[i] <= source[j] or j > end ), 
        # it gets index out of bound exception when calling source[i] <= source[j], 
        # because j > end is short-cut conditions
        # put short-cut conditions in front whenever possible
        if i < mid and ( j > end or source[i] <= source[j] ):
            target[targetIdx] = source[i]
            i += 1
        else:
            target[targetIdx] = source[j]
            j += 1
        targetIdx += 1

def merge_sort_topdown(source,start,end,target):
    '''Merge sort.
    
    Topdown method, use recursive algorithm'''
    if end > start:
        mid = int((start+end)/2)  # since int() uses floor() by default
        # things are tricky here,thinking that target always holds the sort result for each recurse
        # while source holds intermediate result
        # At the beginning, both source and target hold the initial array 
        merge_sort_topdown(target, start, mid, source)
        # use as less minus operation on array index as possible, so as to avoid negtive index
        merge_sort_topdown(target, mid+1, end, source)
        merge(source, start, mid+1, end, target)

def merge_sort_bottomup_onepass(source, length, target):
    '''Merge 2 parts of length "step" if possible, starting index is "start"'''
    i = 0
    end = len(source) - 1
    while i + 2*length <= end:
        merge(source, i, i+length, i+2*length -1, target)
        i += 2 * length
    
    if  i + length <= end:
        merge(source, i, i+length, end, target)
    else:
        for i in range(i,end+1):
            target[i] = source[i]

def merge_sort_bottomup(source, start, end, target):
    '''Merge sort.
    
    Bottomup method'''
    step = 1
    end = len(source) -1
    while step <= end:
        merge_sort_bottomup_onepass(source, step, target)
        step *= 2
        merge_sort_bottomup_onepass(target, step, source)       
            

source = copy.deepcopy(testdata.dataset1)
print("original set:\t", source)
target = copy.deepcopy(source)

print(merge_sort_topdown.__doc__)
merge_sort_topdown(target, 0, len(target)-1, source)
print("after {}:\t{}".format(merge_sort_topdown.__name__, source))  

source = copy.deepcopy(testdata.dataset1)
print("original set:\t", source)
target = copy.deepcopy(source)

print(merge_sort_bottomup.__doc__)
merge_sort_bottomup(target, 0, len(target)-1, source)
print("after {}:\t{}".format(merge_sort_bottomup.__name__, source))  

