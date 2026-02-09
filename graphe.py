class graphe:
    def __init__(self, sommet):
        self.neighbors = dict() ## dico regroupant tous les sommets du graphe, clés sont les sommets et valeur un dico voir plus bas 
        for s in sommet:
            self.neighbors[s] = [False] ## clés sont les voisins et valeurs une liste format [True/False, [voisins]]

    def append_neighbors(self, s, neighbors):
        self.neighbors[s].append(neighbors)
                                
    def neighbors(self, s):
        return self.neighbors[s][1]  ## renvoie la liste des voisins du sommet 
    
    def is_neighbors(self, s1, s2):
        return s1 in self.neighbors[s2][1]
    
    def is_infected(self,s):
        return self.neighbors[s][0]
    
    def __str__(self):
        return f"{self.neighbors}"
    

bite = graphe(["A", "B", "C"])
print(bite)
bite.append_neighbors("A", ["B", "C"])
print(bite)

print(bite.is_infected("A"))

