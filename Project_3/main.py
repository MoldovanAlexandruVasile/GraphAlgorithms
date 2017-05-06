from Graph import *
from Dijkstra import *

def accessible(g, s):
    """
    Returns the set of vertices of the graph g that are accessible
    from the vertex s
    """
    acc = set()
    acc.add(s)
    list = [s]
    while len(list) > 0:
        x = list[0]
        list = list[1:]
        for y in g.parseNout(x):
            if y not in acc:
                acc.add(y)
                list.append(y)
    return acc

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
        g = DoubleDictGraph(n_vertex)
        line = edgesFile.readline().strip()
        while line != "":
            lx = line.split(' ')
            g.addEdge(int(lx[0]), int(lx[1]), int(lx[2]))
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
            for j in graph.parseNout(i):
                s = str(i) + ' ' + str(j) + ' ' + str(graph.getCost(int(i),int(j))) + '\n'
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
    print("      6. Update the cost of an edge.")
    print("      7. Total number of vertexes.")
    print("      8. Total number of edges.")
    print("      9. Check if there is an edge from two vertices.")
    print("     10. Get the IN and OUT degree of a vertex.")
    print("     11. Accessible vertices from a given vertex.")
    print("     12. Outbound neighbours of a given vertex.")
    print("     13. Inbound neighbours of a given vertex.")
    print("     14. Isolated vertices.")
    print("     15. Dijkstra")
    print("      0. Exit.\n")

def printGraph(graph):
    '''
    :param graph: The graph we want to print
    :return: The current graph outputed on the screen
    '''
    print("\n===================")
    for x in graph.parseX():
        print("%s:" % x)
        for y in graph.parseNout(x):
            print("%s -> %s with cost %s" % (x, y, graph.getCost(x,y)))
        print("===================")


#===========================MAIN===========================

def run():

    g = readGraphFile(DoubleDictGraph)[0]
    n_vertex = int(readGraphFile(DoubleDictGraph)[1])
    m_edges = int(readGraphFile(DoubleDictGraph)[2])
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
                        writeToGraphFile(g,n_vertex,m_edges)
                        print("\n     Vertex added ! \n")
                    else: print("\n     Vertex already exists ! \n")

            elif command == 3:
                edgeFrom = input("\n     Edge from: ")
                edgeTo = input("\n     Edge to: ")
                if validInteger(edgeFrom) and validInteger(edgeTo):
                    if g.isVertex(int(edgeFrom)) and g.isVertex(int(edgeTo)):
                        if g.isEdge(int(edgeFrom), int(edgeTo)) == False:
                            cost = input("\n     Cost: ")
                            if validInteger(cost):
                                g.addEdge(int(edgeFrom), int(edgeTo), int(cost))
                                m_edges = m_edges + 1
                                writeToGraphFile(g, n_vertex, m_edges)
                                print("\n     Edge added !\n")
                            else: print("\n     Invalid cost ! \n")
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
                    else: print("\n     Invalid data !")
                else: print("\n     Invalid data !")

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

            elif command == 7:
                print("\n     Total number of vertexes:",n_vertex,"\n")

            elif command == 8:
                print("\n     Total number of edges:",m_edges,"\n")

            elif command == 9:
                edgeFrom = input("\n     Edge from: ")
                edgeTo = input("\n     Edge to: ")
                if validInteger(edgeFrom) and validInteger(edgeTo):
                    if g.isVertex(int(edgeFrom)) and g.isVertex(int(edgeTo)):
                        lx = g.parseNout(int(edgeFrom))
                        if int(edgeTo) in lx:
                            print("\n     There is an edge between those vertices with cost", g.getCost(int(edgeFrom),int(edgeTo)),"!\n")
                        else: print("\n     There not exist an edge between those vertices !\n")
                    else: print("\n     Invalid data !")
                else: print("\n     Invalid data !")

            elif command == 10:
                vertex = input("\n     Vertex: ")
                if validInteger(vertex):
                    if g.isVertex(int(vertex)):
                        lx = g.parseNout(int(vertex))
                        print("\n     OUT degree:",len(lx))
                        lx = g.parseNin(int(vertex))
                        print("\n     IN degree:", len(lx))
                    else: print("\n     Invalid data !")
                else: print("\n     Invalid data !")

            elif command == 6:
                edgeFrom = input("\n     Edge from: ")
                edgeTo = input("\n     Edge to: ")
                if validInteger(edgeFrom) and validInteger(edgeTo):
                    if g.isVertex(int(edgeFrom)) and g.isVertex(int(edgeTo)):
                        lx = g.parseNout(int(edgeFrom))
                        if int(edgeTo) in lx:
                            cost = input("\n     Cost: ")
                            if validInteger(cost):
                                g.setCost(int(edgeFrom),int(edgeTo), int(cost))
                                writeToGraphFile(g, n_vertex, m_edges)
                                print("\n     Updated !")
                            else: print("\n     Invalid data !")
                        else: print("\n     There not exist an edge between those vertices !\n")
                    else: print("\n     Invalid data !")
                else: print("\n     Invalid data !")
            elif command == 11:
                vertex = input("\n     Vertex: ")
                if validInteger(vertex):
                    if g.isVertex(int(vertex)):
                        print("\n     Accesible vertices:", accessible(g, int(vertex)))
                    else: print("\n     No such vertex !")
                else: print("\n     Invalid data !")
            elif command == 12:
                vertex = input("\n     Vertex: ")
                if validInteger(vertex):
                    if g.isVertex(int(vertex)):
                        print("\n     Outbound neigbours of",vertex,"are:", g.parseNout(int(vertex)))
                    else: print("\n     No such vertex !")
                else: print("\n     Invalid data !")
            elif command == 13:
                vertex = input("\n     Vertex: ")
                if validInteger(vertex):
                    if g.isVertex(int(vertex)):
                        print("\n     Inbound neigbours of",vertex,"are:", g.parseNin(int(vertex)))
                    else: print("\n     No such vertex !")
                else: print("\n     Invalid data !")
            elif command == 14:
                s = ''
                for x in g.parseX():
                    if g.parseNin(x) == [] and g.parseNout(x) == []:
                        s = s + ' ' + str(x)
                if s != '': print("\n     Isolated vertices:",s)
                else: print("\n     There are no isolated vertices !\n")
            elif command == 15:
                edgeFrom = input("\n     Start: ")
                edgeTo = input("\n     End: ")
                if validInteger(edgeFrom) and validInteger(edgeTo):
                    if g.isVertex(int(edgeFrom)) and g.isVertex(int(edgeTo)):
                        dijkstra(g, int(edgeFrom), int(edgeTo))
            else:
                if command != 0:
                    print("\n     Invalid data !")


run()