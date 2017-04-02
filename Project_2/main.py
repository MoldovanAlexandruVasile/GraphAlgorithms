from Graph import *


def readGraphFile(ctor):
    """
    Reads the graph from the file Edges.txt
    """
    try:
        edgesFile = open("EdgesInput.txt", "r")
        line = edgesFile.readline().strip()
        lx = line.split(' ')
        n_vertex = int(lx[0])
        m_edges = int(lx[1])
        g = DictGraph(n_vertex)
        line = edgesFile.readline().strip()
        while line != "":
            lx = line.split(' ')
            g.addEdge(int(lx[0]), int(lx[1]))
            line = edgesFile.readline().strip()
        edgesFile.close()
        return [g, int(n_vertex), int(m_edges)]
    except IOError: pass


def writeToGraphFile(graph,n,m):
    '''
    Writes the current graph in a file
    '''

    edgesFile = open("EdgesOutput.txt", "w")
    try:
        s = str(n) + " " + str(m) + "\n"
        edgesFile.write(s)
        for i in graph.parseX():
            for j in graph.parseN(i):
                if i <= j:
                    s = str(i) + ' ' + str(j) + '\n'
                    edgesFile.write(s)
        edgesFile.close()
    except Exception as e: print('\t \n', e)


def validInteger(x):
    '''
    :param x: The input that we want to test if it is a integer number
    :return: True - if the number it is integer and valid
             False - if the number it is not a number
    '''
    try:
        cmd = int(x)
        return True
    except ValueError:
        print("\n     Invalid data ! \n")
        return False


def printGraph(graph):
    '''
    :param graph: The graph we want to print
    :return: The current graph outputed on the screen
    '''
    print("\n===================")
    for x in graph.parseX():
        print("%s:" % x)
        for y in graph.parseN(x):
            print("%s - %s " % (x, y,))
        print("===================")

def printMenu():
    '''
    :return: The menu output.
    '''
    print("\n           ~Menu~\n")
    print("      1. Print graph.")
    print("      2. Add a new vertex.")
    print("      3. Add a new edge.")
    print("      4. Delete a vertex.")
    print("      5. Delete an edge.")
    print("      6. Total number of vertexes.")
    print("      7. Total number of edges.")
    print("      8. Isolated vertices.")
    print("      9. Check if there is an edge from two vertices.")
    print("     10. DFS traversal.")
    print("      0. Exit.\n")


#===========================MAIN===========================
def run():
    g = readGraphFile(DictGraph)[0]
    n_vertex = int(readGraphFile(DictGraph)[1])
    m_edges = int(readGraphFile(DictGraph)[2])
    command = -1
    while command != 0:
        printMenu()
        command = input("\n Your command: ")
        if validInteger(command) == True:
            command = int(command)
            if command == 1:
                printGraph(g)
            elif command == 2:
                vertex = input("\n     Vertex: ")
                if validInteger(vertex):
                    if g.isVertex(int(vertex)) == False:
                        g.addVertex(int(vertex))
                        n_vertex = n_vertex + 1
                        writeToGraphFile(g, n_vertex, m_edges)
                        print("\n     Vertex added ! \n")
                    else: print("\n     Vertex already exists ! \n")

            elif command == 3:
                edgeFrom = input("\n     Edge from: ")
                edgeTo = input("\n     Edge to: ")
                if validInteger(edgeFrom) and validInteger(edgeTo):
                    if g.isVertex(int(edgeFrom)) and g.isVertex(int(edgeTo)):
                        if g.isEdge(int(edgeFrom), int(edgeTo)) == False:
                            g.addEdge(int(edgeFrom), int(edgeTo))
                            m_edges = m_edges + 1
                            writeToGraphFile(g, n_vertex, m_edges)
                            print("\n     Edge added !\n")
                        else: print("\n     Edge already exists !")
                    else: print("\n     Invalid data ! \n")
                else: print("\n     Invalid data ! \n")

            elif command == 4:
                vertex = input("\n     Vertex: ")
                if validInteger(vertex):
                    if g.isVertex(int(vertex)):
                        m_edges = g.removeVertex(int(vertex), int(m_edges))
                        n_vertex = n_vertex - 1
                        writeToGraphFile(g, n_vertex, m_edges)
                        print("\n     Deleted !")
                    else:
                        print("\n     Invalid data !")
                else:
                    print("\n     Invalid data !")

            elif command == 5:
                edgeFrom = input("\n     Edge from: ")
                edgeTo = input("\n     Edge to: ")
                if validInteger(edgeFrom) and validInteger(edgeTo):
                    if g.isVertex(int(edgeFrom)) and g.isVertex(int(edgeTo)):
                        g.removeEdge(int(edgeFrom), int(edgeTo))
                        m_edges = m_edges - 1
                        writeToGraphFile(g, n_vertex, m_edges)
                        print("\n     Deleted !")
                    else: print("\n     Invalid data !")
                else: print("\n     Invalid data !")

            elif command == 6:
                print("\n     Total number of vertexes:", n_vertex, "\n")

            elif command == 7:
                print("\n     Total number of edges:", m_edges, "\n")

            elif command == 8:
                s = ''
                for x in g.parseX():
                    if g.parseN(x) == [] :
                        s = s + '  ' + str(x)
                if s != '': print("\n     Isolated vertices:",s)
                else: print("\n     There are no isolated vertices !\n")
            elif command == 9:
                edgeFrom = input("\n     Edge from: ")
                edgeTo = input("\n     Edge to: ")
                if validInteger(edgeFrom) and validInteger(edgeTo):
                    if g.isVertex(int(edgeFrom)) and g.isVertex(int(edgeTo)):
                        lx = g.parseN(int(edgeFrom))
                        if int(edgeTo) in lx:
                            print("\n     There is an edge between those vertices !\n")
                        else: print("\n     There not exist an edge between those vertices !\n")
                    else: print("\n     Invalid data !")
                else: print("\n     Invalid data !")
            elif command == 10:
                vertex = input("\n     Vertex you want to start: ")
                if validInteger(vertex):
                    if g.isVertex(int(vertex)):
                        print(" ")
                        g.DFS(int(vertex))
                    else: print("\n     Invalid vertex ! \n")
                else: print("\n     Invalid data !\n")
run()