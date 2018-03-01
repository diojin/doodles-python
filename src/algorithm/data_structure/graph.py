from queue import Queue

class AdjacentMatrixGraph:
    def __init__(self, edges, vertexList=None):
        self.edges = edges
        self.vertexList = vertexList
    
    def eachVertexesMinDist(self):
        size = len(self.edges)
        dist = [[float('inf') for i in range(0, size)] for j in range(0,size)]
        path = [[-1 for i in range(0, size)] for j in range(0,size)]
        for i in range(0, size):
            for j in range(0, size):
                if self.edges[i][j] > 0:
                    dist[i][j] = self.edges[i][j]
                    path[i][j] = i
        
        for k in range(0, size):
            for i in range(0, size):
                if i != k:
                    for j in range(0, size):
                        if j != k and i != j and dist[i][k]< float('inf') \
                        and dist[k][j] < float('inf') and dist[i][k] + dist[k][j] < dist[i][j]:
                            dist[i][j] = dist[i][k] + dist[k][j]
                            path[i][j] = path[k][j]
        return dist

class AdjacentArrayGraph:
    def __init__(self, vertexes):
        self.vertexes = vertexes
        self.visitCount = {}
        for i in vertexes:
            self.visitCount[i.verName] = 0
    
    def resetVisitCount(self):
        for i in vertexes:
            self.visitCount[i.verName] = 0
    
    def depthFirstSearch(self, startAdj):
        if self.visitCount[startAdj] == 0 :
            print(vertexes[startAdj])
            self.visitCount[startAdj] = 1
            edge = vertexes[startAdj].next
            while edge:
                self.depthFirstSearch(edge.verAdj)
                edge = edge.next
    
    def depthFirstSearchStack(self, startAdj):
        '''Depth first search implemented by stack
        
        Simple and elegant.'''
        stack = []
        stack.append(startAdj)
        while len(stack) > 0:
            ver = stack.pop()
            if self.visitCount[ver] == 0:
                print(vertexes[ver])
                self.visitCount[ver] = 1
                reverseLink = []
                edge = vertexes[ver].next
                while edge:
                    reverseLink.insert(0,edge)
                    edge = edge.next
                for i in reverseLink:
                    stack.append(i.verAdj)
    
    def depthFirstSearchStack1(self, startAdj):
        '''Depth first search implemented by stack
        
        Another implementation,not that good.'''
        stack= []
        cur = vertexes[startAdj]
        while len(stack) > 0 or cur:
            while cur and self.visitCount[cur.verName] == 0:
                print(cur)
                self.visitCount[cur.verName] = 1
                stack.append(cur)
                edge = cur.next
                if edge:
                    cur = vertexes[edge.verAdj]
                else:
                    cur = None
                
            cur = stack.pop()
            # check if all adjacent nodes are visited, 
            # or else, push it back
            if cur:
                adj = cur.next
                while adj and self.visitCount[adj.verAdj] == 1:
                    adj = adj.next
                if adj:
                    stack.append(cur)
                    cur = vertexes[adj.verAdj]
                else:
                    cur = None
    
    def widthFirstSearch(self, startAdj):
        self.resetVisitCount()
        queue = Queue()
        queue.put(vertexes[startAdj], False)
        while not queue.empty():
            ver = queue.get(False)
            if ver and self.visitCount[ver.verName]==0:
                print(ver)
                self.visitCount[ver.verName] = 1
                edge = ver.next
                while edge:
                    if self.visitCount[edge.verAdj] == 0:
                        queue.put_nowait(vertexes[edge.verAdj])
                    edge = edge.next
    def topologicalSort(self):
        indegree = [0 for i in vertexes]
        # top points to the top of zero indegree vertex stack
        top = -1
        for i in vertexes:
            edge = i.next
            while edge:
                indegree[edge.verAdj] += 1
                edge = edge.next
        for i in indegree:
            if indegree[i] == 0:
                print(vertexes[i])
                # in stack operation
                indegree[i] = top
                top = i
        
        while top != -1:
            # out stack operation
            curIdx = top
            top = indegree[top]
            edge = vertexes[curIdx].next
            while edge:
                indegree[edge.verAdj] -= 1
                if indegree[edge.verAdj] == 0:
                    print(vertexes[edge.verAdj])
                    # in stack operation
                    indegree[edge.verAdj] = top
                    top = edge.verAdj
                edge = edge.next   
    def topologicalSortWithCircuitDetect(self):
        indegree = [0 for i in vertexes]
        # top points to the top of zero indegree vertex stack
        top = -1
        for i in vertexes:
            edge = i.next
            while edge:
                indegree[edge.verAdj] += 1
                edge = edge.next
        for i in indegree:
            if indegree[i] == 0:
                # in stack operation
                indegree[i] = top
                top = i
        
        for i in range(0, len(vertexes)):
            if top != -1:
                # out stack operation
                curIdx = top
                top = indegree[top]
                print(vertexes[curIdx])
                edge = vertexes[curIdx].next
                while edge:
                    indegree[edge.verAdj] -= 1
                    if indegree[edge.verAdj] == 0:
                        # in stack operation
                        indegree[edge.verAdj] = top
                        top = edge.verAdj
                    edge = edge.next
            else:
                raise Exception("there is a circuit")
            

class VertexNode:
    def __init__(self, verName,next = None):
        '''Initialization method.
        
        verName is the data of the vertex.
        next is pointer to EdgeNod.'''
        self.verName = verName
        self.next = next
    def __str__(self):
        return "[verName={},{}]".format(self.verName, self.next is None)
    
    def __hash__(self):
        return self.verName.__hash__

class EdgeNode:
    def __init__(self, verAdj, weight = -1, next = None  ):
        '''Initialization method.
        
        verAdj is the verName of adjacent node.
        next is pointer to next EdgeNode
        weight is the weight of the edge'''
        self.verAdj = verAdj
        self.next = next
        self.weight = weight
    def __str__(self):
        return "[verAdj={},weight={},{}]".format(self.verAdj, self.weight, self.next is None)
        
# AOE Graph Example:
#                        T1                                                    T6
#                     ^     \                                             ^          \
#                  /               a3=1                                /                   a10=2
#          a0=6                            \               a7=9                                    \
#      /                                     v         /                                            v
# T0                                           T4                                                   T8
# \        \                                ^       \                                             ^
#  \        1=4                        /                a8=8                                   /
#   \          \                a4=1                           \                       a11=4
#      \         v             /                                v           /
#       \           T2                                              T7
#          \                \                                     ^
#          a2=5             a5=1                               /
#              \                       \                a9=4
#              \                        v            /   
#              \                            T5
#                \                        ^
#                  \                    /
#                   \              a6=2
#                     v      /
#                      T3

# test data is here.

vers = [0, 1, 2, 3, 4, 5, 6, 7, 8]

matrix =[
   #[0, 1, 2, 3, 4, 5, 6, 7, 8]
    [0, 6, 4, 5, 0, 0, 0, 0, 0], #0
    [0, 0, 0, 0, 1, 0, 0, 0, 0], #1
    [0, 0, 0, 0, 1, 1, 0, 0, 0], #2
    [0, 0, 0, 0, 0, 2, 0, 0, 0], #3
    [0, 0, 0, 0, 0, 0, 9, 8, 0], #4
    [0, 0, 0, 0, 0, 0, 0, 4, 0], #5
    [0, 0, 0, 0, 0, 0, 0, 0, 2], #6
    [0, 0, 0, 0, 0, 0, 0, 0, 4], #7
    [0, 0, 0, 0, 0, 0, 0, 0, 0]  #8    
]

aoeMatrixGraph = AdjacentMatrixGraph(matrix, vers)

vertexes = []

edge = EdgeNode(1, 6, 
              EdgeNode(2, 4,
                  EdgeNode(3, 5, None)))
vertexes.append(VertexNode(0, edge))  

edge = EdgeNode(4, 1, None)
vertexes.append(VertexNode(1, edge))

edge = EdgeNode(4, 1, 
          EdgeNode(5, 1, None))
vertexes.append(VertexNode(2, edge))

edge = EdgeNode(5, 2, None)
vertexes.append(VertexNode(3, edge))

edge = EdgeNode(6, 9,
          EdgeNode(7, 8, None))              
vertexes.append(VertexNode(4, edge))

edge = EdgeNode(7, 4, None)
vertexes.append(VertexNode(5, edge))

edge = EdgeNode(8, 2, None)
vertexes.append(VertexNode(6, edge))

edge = EdgeNode(8, 4, None)
vertexes.append(VertexNode(7, edge))

vertexes.append(VertexNode(8, None))   

aoeGraph = AdjacentArrayGraph(vertexes)

# test start here
print("depth first search")
aoeGraph.depthFirstSearch(0)

print("depth first search via stack")
aoeGraph.resetVisitCount()
aoeGraph.depthFirstSearchStack(0)

print("depth first search via stack 1")
aoeGraph.resetVisitCount()
aoeGraph.depthFirstSearchStack1(0)

print("width first search")
aoeGraph.widthFirstSearch(0)

print("topological sort")
aoeGraph.topologicalSort()
aoeGraph.topologicalSortWithCircuitDetect()

print("shortest path for each pair of vertexes")
dist = aoeMatrixGraph.eachVertexesMinDist()
print(dist)

