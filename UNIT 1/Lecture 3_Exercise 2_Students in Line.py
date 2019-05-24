class Node(object):
    def __init__(self, name):
        """Assume name is a string"""
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name


class Edge(object):
    def __init__(self, src, dest):
        """Assumes src(Source) and dest(Destination) are nodes"""
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDest(self):
        return self.dest
    def __str__(self):
        return self.src.getName() + '->'+ self.dest.getName()


class Digraph(object):
    """edges is a dict mapping each node to a list of its children"""

    def __init__(self):
        self.edges = {}

    def addNode(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDest()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def childrenof(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.edges

    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)

    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + '->' + dest.getName() + '\n'
        return result[:-1] # Omit final newline


class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDest(), edge.getSource())
        Digraph.addEdge(self, rev)


nodes = []
nodes.append(Node("ABC")) # nodes[0]
nodes.append(Node("ACB")) # nodes[1]
nodes.append(Node("BAC")) # nodes[2]
nodes.append(Node("BCA")) # nodes[3]
nodes.append(Node("CAB")) # nodes[4]
nodes.append(Node("CBA")) # nodes[5]

g = Graph()
for n in nodes:
    g.addNode(n)


# i = -1
# for n in nodes:
#     i += 1
#     a = n.getName()[0] + n.getName()[2] + n.getName()[1]
#     b = n.getName()[1] + n.getName()[0] + n.getName()[2]
#     for nrest in nodes[i:]:
#         if a == nrest.getName() or b == nrest.getName():
#             e = Edge(n, nrest)
#             g.addEdge(e)




for node in nodes:
    n = node.getName()
    for other_node in nodes:
        if other_node.getName() == n[1]+n[0]+n[2] or other_node.getName() == n[0]+n[2]+n[1]:
            Digraph.addEdge(g, Edge(node, other_node))


print(g)


