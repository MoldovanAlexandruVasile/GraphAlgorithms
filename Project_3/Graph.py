class DoubleDictGraph:
    """
    A directed graph, represented as two maps,
    one from each vertex to the set of outbound neighbours,
    the other from each vertex to the set of inbound neighbours
    """

    def __init__(self, n):
        """
        Creates a graph with n vertices (numbered from 0 to n-1)
        and no edges
        """

        self._dictOut = {}
        self._dictIn = {}
        self._cost = {}
        for i in range(n):
            self._dictOut[i] = []
            self._dictIn[i] = []

    def parseX(self):
        """
        Returns an iterable containing all the vertices
        """
        return self._dictOut.keys()

    def parseNout(self, x):
        """
        Returns an iterable containing the outbound neighbours of x
        """
        return self._dictOut[x]

    def parseNin(self, x):
        """
        Returns an iterable containing the inbound neighbours of x
        """
        return self._dictIn[x]

    def isEdge(self, x, y):
        """
        Returns True if there is an edge from x to y, False otherwise
        """
        return y in self._dictOut[x]

    def addEdge(self, x, y, cost):
        """
        Adds an edge from x to y.
        """
        self._dictOut[x].append(y)
        self._dictIn[y].append(x)
        self._cost[(x,y)] = cost

    def addVertex(self,x):
        '''
        Adds a new vertex to the graph
        :param x: The vertex we want to add
        '''
        self._dictOut[x] = []
        self._dictIn[x] = []

    def isVertex(self,x):
        '''
        Checks if the vertex does exists
        :param x: the vertex we check for
        '''
        return x in self._dictIn.keys()

    def getCost(self,x,y):
        '''
        :param x: Edge from
        :param y: Edge to
        :return: the cost of the edge (x, y)
        '''
        return self._cost[(x,y)]

    def setCost(self,x, y, cost):
        '''
        :param x: Edge from
        :param y: Edge to
        :param cost: the cost of the edge (x, y)
        '''
        self._cost[(x,y)] = cost

    def removeVertex(self, x, m_edges):
        '''
        :param x: The vertex
        :return: the graph without that vertex
        '''
        ok = True
        while ok == True:
            ok = False
            for i in self.parseNin(int(x)):
                if self.isEdge(int(i), int(x)):
                    self.removeEdge(int(i), int(x))
                    m_edges = m_edges - 1
                    ok = True
            for i in self.parseNout(int(x)):
                if self.isEdge(int(x), int(i)):
                    self.removeEdge(int(x), int(i))
                    m_edges = m_edges - 1
                    ok = True
        self._dictIn.pop(x)
        self._dictOut.pop(x)
        return int(m_edges)


    def removeEdge(self, x, y):
        '''
        :param x: Edge from
        :param y: Edge to
        :return: The graph without the edge
        '''

        self._dictOut[x].remove(y)
        self._dictIn[y].remove(x)
        self._cost.pop((x,y))