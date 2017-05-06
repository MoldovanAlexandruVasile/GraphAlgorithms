from Graph import *

class PriorityQueue:
    def __init__(self):
        self.__values = {}

    def isEmpty(self):
        return len(self.__values) == 0

    def pop(self):
        topPriority = None
        topObject = None
        for obj in self.__values:
            objPriority = self.__values[obj]
            if topPriority is None or topPriority > objPriority:
                topPriority = objPriority
                topObject = obj
        del self.__values[topObject]
        return topObject

    def add(self, obj, priority):
        self.__values[obj] = priority

    def contains(self, val):
        return val in self.__values


def dijkstra(g, start, end):
    prev = {}
    q = PriorityQueue()
    q.add(start, 0)
    d = {}
    d[start] = 0
    visited = set()
    visited.add(start)
    k = 0
    while not q.isEmpty():
        x = q.pop()
        for y in g.parseNout(x):
            if (y not in visited or d[y] > d[x] + g.getCost(x, y)):
                d[y] = d[x] + g.getCost(x, y)
                visited.add(y)
                q.add(y, d[y])
                prev[y] = x
            if y == end:
                k = 1
                break
    if k == 0: print("\n\t Unreacheble two vertices !")
    else:
        path=[]
        while end!=start:
            path.append(end)
            end=prev[end]
        path.append(start)
        path.reverse()
        print("\n\t\tMinimum cost PATH:",path)