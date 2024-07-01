for otrezok in range(185311, 185330+1):
    massiv = []
    for delenie in range(2, 185330+1):
        if otrezok % delenie == 0:
            massiv.append(delenie)
            if len(massiv) == 4:
                print(*massiv)