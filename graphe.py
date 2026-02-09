class graphe:
    def __init__(self, sommet):
        self.neighbors = dict() ## dico regroupant tous les sommets du graphe, clés sont les sommets et valeur un dico voir plus bas 
        for s in sommet:
            self.neighbors[s] = [False] ## clés sont les voisins et valeurs les poids de la relation, plus le poids est important plus la proba de contaminer est importante
                                
    def neighbors(s):
        return self.neighbors[s][1]  ## renvoie la liste des voisins du sommet 
    
    def is_neighbors(s1, s2):
        return s1 in self.neighbors[s2][1]
    
    def __str__(self):
        return f"{self.neighbors}"
    

bite = graphe(["A", "B", "C"])
print(bite)