def TowerOfHanoi(n, source, destination_rod, auxilliary_rod):
    if n ==1:
        print("Have disk 1 from source:", source, " to destination ", destination_rod)
        return
    TowerOfHanoi(n-1, source, auxilliary_rod, destination_rod)
    print("Move disk", n, " from source ",source, "to destination", destination_rod)
    TowerOfHanoi(n-1, auxilliary_rod, destination_rod, source)

n=3
TowerOfHanoi(n,'A','B','C')