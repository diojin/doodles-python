
# coding: utf-8

# In[23]:


pattern = "abab"
target1 = "abaaabab"
target2 = "waba eesw"

def failureFunction(matchingString):
    failure=[-1 for i in matchingString]
    for i in range(1, len(matchingString)):
        cur = i
        while cur > 0 and matchingString[failure[cur-1]+1] != matchingString[i]:
            cur = failure[cur-1]
        if cur <= 0:
            failure[i] = -1
        else:
            failure[i] = failure[cur-1] + 1dd
    return failure

def kmpFastMatch(source, pattern):
    fail = failureFunction(pattern)
    p = 0
    s = 0
    while p < len(pattern) and s < len(source):
        if pattern[p] == source[s]:
            p += 1
            s += 1
        elif p > 0:
            p = fail[p-1] + 1
        else:
            p = 0
            s += 1
    if p == len(pattern):
        return s-p
    else:
        return -1


res = failureFunction(pattern)
print(res)
print(kmpFastMatch(target1, pattern))


# print all possible substring combination of a string
# for example, for 'abc', result is c,b,bc,a,ac,ab,abc

def __strPrinter(strArray, endIndex, delimiter = ''):
    '''endIndex is inclusive'''
    return delimiter.join(strArray[:endIndex+1])

def substrCombinationInternal(source,curStrIndex,stackIndex, stack):
    '''It has 2^n stack invocation.'''
    if curStrIndex == len(source):
        stackIndex -= 1
        # it is very important to restrain the upper bound of result
        # since data beyond it is garbage from previous round of computation
        if stackIndex >= 0:
            print(__strPrinter(stack, stackIndex))
    else:
        substrCombinationInternal(source,curStrIndex+1,stackIndex, stack)
        stack[stackIndex] = source[curStrIndex]
        substrCombinationInternal(source,curStrIndex+1, stackIndex+1, stack)

def substrCombination(source):
    substrCombinationInternal(source, 0, 0,['' for i in range(0, len(source))])

substrCombination('abcd')        


    

