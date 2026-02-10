class Node:
    def __init__(self, neighbors=[]):
        self.infected = False
        self.neighbors = neighbors

class Graphe:
    def __init__(self, n:int=0):
        self.nodes = {i:Node() for i in range(n)}

    @staticmethod
    def from_list(lst):
        """Create graph from adjacency list with indices"""
        g = Graphe(len(lst))
        for i, neighbors in enumerate(lst):
            g.nodes[i].neighbors = neighbors
        return g

    @staticmethod
    def from_dict(d):
        """Create graph from dictionary with node names
        EXAMPLE:
            graph = {
            "A": ["B", "C"],
            "B": ["A", "C", "D"],
            "C": ["A", "B"],
            "D": ["B", "E", "F"],
            "E": ["D", "F"],
            "F": ["D", "E", "G"],
            "G": ["F"],
        }
        """
        g = Graphe()
        for name, neighbors in d.items():
            g.nodes[name] = Node(neighbors)
        return g

    def get_node(self, index_or_name):
        """Get node by index or name"""
        if isinstance(index_or_name, int):
            return self.nodes[index_or_name]
        else:
            for node in self.nodes:
                if node.name == index_or_name:
                    return node
            return None

    def append_neighbors(self, index_or_name, neighbors):
        """Add neighbors to a node"""
        node = self.get_node(index_or_name)
        if node:
            node.neighbors.extend(neighbors)
                                
    def get_neighbors(self, index_or_name):
        """Return the list of neighbors for a node"""
        node = self.get_node(index_or_name)
        if node:
            return node.neighbors
        return []
    
    def infect(self, index_or_name):
        """Mark a node as infected"""
        node = self.get_node(index_or_name)
        if node:
            node.infected = True

    def is_neighbors(self, node1, node2):
        """Check if node1 and node2 are neighbors"""
        n1 = self.get_node(node1)
        n2 = self.get_node(node2)
        if n1 and n2:
            return n2.name in n1.neighbors or n2 in n1.neighbors
        return False
    
    def is_infected(self, index_or_name):
        """Check if a node is infected"""
        node = self.get_node(index_or_name)
        if node:
            return node.infected
        return False
    
    def __str__(self):
        result = "Graph:\n"
        for i, node in enumerate(self.nodes):
            result += f"  Node {node.name or i}: infected={node.infected}, neighbors={node.neighbors}\n"
        return result

