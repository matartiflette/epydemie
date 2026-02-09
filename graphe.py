class graphe:
    def __init__(self, sommet):
        self.all_summit = dict() ## tous les sommets du graphe, clés sont les sommets et valeur un dico 
        for s in sommet:
            self.all_summit[s] = [False] ## clés sont les voisins et valeurs une liste format [True/False, [voisins]]

    def append_neighbors(self, s, neighbors):
        self.all_summit[s].append(neighbors)
                                
    def all_summit(self, s):
        return self.all_summit[s][1]  ## renvoie la liste des voisins du sommet
    
    def infect(self, s):
        self.all_summit[s][0] = True

    def is_neighbors(self, s1, s2):
        return s1 in self.all_summit[s2][1]
    
    def is_infected(self,s):
        return self.all_summit[s][0]
    
    def __str__(self):
        return f"{self.all_summit}"
    

bite = graphe(["A", "B", "C"])
print(bite)
bite.append_neighbors("A", ["B", "C"])
print(bite)

print(bite.is_infected("A"))

