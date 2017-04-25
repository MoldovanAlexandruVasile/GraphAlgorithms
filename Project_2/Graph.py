import sys

class DictGraph:
    """
    An undirected graph, represented as a map from each vertex to
    the set of outbound neighbours
    """

    def __init__(self, n):
        """
        Creates a graph with n vertices (numbered from 0 to n-1)
        and no edges
        """
        self._dict = {}
        for i in range(n):
            self._dict[i] = []

    def parseX(self):
        """
        Returns an iterable containing all the vertices
        """
        return self._dict.keys()

    def parseN(self, x):
        """
        Returns an iterable containing the neighbours of x
        """
        return self._dict[x]

    def isEdge(self, x, y):
        """
        Returns True if there is an edge from x to y (respectivly y to x), False otherwise
        """
        return y in self._dict[x] and x in self._dict[y]

    def addEdge(self, x, y):
        """
        Adds an edge from x to y.
        """
        self._dict[x].append(y)
        self._dict[y].append(x)

    def addVertex(self,x):
        """
        Adds a new vertex to the graph
        :param x: The vertex we want to add
        """
        self._dict[x] = []

    def isVertex(self,x):
        """
        Checks if the vertex does exists
        :param x: the vertex we check for
        """
        return x in self._dict.keys()

    def removeVertex(self, x, m_edges):
        """
        :param x: The vertex
        :return: the graph without that vertex
        """
        ok = True
        while ok == True:
            ok = False
            for i in self.parseN(int(x)):
                if self.isEdge(int(i), int(x)):
                    self.removeEdge(int(i), int(x))
                    m_edges = m_edges - 1
                    ok = True
        self._dict.pop(x)
        return int(m_edges)

    def removeEdge(self, x, y):
        """
        :param x: Edge from
        :param y: Edge to
        :return: The graph without the edge
        """

        self._dict[x].remove(y)
        self._dict[y].remove(x)

    def DFSRec(self, v, visited):
        """
        Mark the current node as visited and print it
        """
        visited[v] = True
        '''Recur for all the vertices adjacent to this vertex'''
        if len(self._dict[v]) == 0:
            print("\t\t", v)
        else:
            for i in self._dict[v]:
                print("\t\t",v, "-", i)
                if visited[i] == False:
                    self.DFSRec(i, visited)

    def DFS(self):
        """
        Mark all the vertices as not visited
        Call the recursive helper function to print DFS traversal
        """
        sys.setrecursionlimit(10000)
        nr = int(0)
        visited = [False] * (len(self._dict))
        for i in self.parseX():
            if visited[i] == False:
                nr = nr + 1
                print("\n A connected component is: ")
                self.DFSRec(i, visited)
        return nr